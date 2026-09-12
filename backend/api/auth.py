#this  file is part of the backend API that handles authentication and authorization for the application. It provides functions to verify JWT tokens, retrieve the current user based on the token, and manage JWKS (JSON Web Key Sets) for asymmetric token verification. The code uses the `fastapi` framework for handling HTTP requests and responses, and the `jwt` library for decoding and verifying JWT tokens.

# jwt token is signed using private key and verfied using public key

#This file handles:“How does the backend check that JWT and decide whether to allow the request?”
import logging
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from backend.core.config import SUPABASE_JWT_SECRET, SUPABASE_URL

logger = logging.getLogger('ats_resume_scorer')

_bearer_scheme = HTTPBearer(auto_error=False)

_ASYMMETRIC_ALGS = ['ES256', 'RS256']

_jwks_client: jwt.PyJWKClient | None = None
#JWKS means:JSON Web Key Set:It is a collection of public keys that can be used to verify JWT signatures.Supabase exposes its public keys through a JWKS endpoint.

def _get_jwks_client() -> jwt.PyJWKClient | None: #This function obtains the JWKS client.
    global _jwks_client    #If the client has already been created, reuse it.
    if _jwks_client is not None:
        return _jwks_client
    if not SUPABASE_URL:
        return None
    jwks_url = f"{SUPABASE_URL.rstrip('/')}/auth/v1/.well-known/jwks.json"
    _jwks_client = jwt.PyJWKClient(jwks_url, cache_keys=True, lifespan=3600) #This creates a client that can retrieve public signing keys from Supabase.
    return _jwks_client


def _verify_token(token: str) -> dict:
    header = jwt.get_unverified_header(token)
    alg = header.get('alg')

    if alg in _ASYMMETRIC_ALGS:
        jwks_client = _get_jwks_client()
        if jwks_client is None:
            raise jwt.InvalidTokenError(
                'SUPABASE_URL not configured — cannot fetch JWKS to verify token'
            )
        signing_key = jwks_client.get_signing_key_from_jwt(token).key  #A JWKS can contain multiple public keys.The JWT header normally contains a key ID (kid) identifying which key was used to sign it.
        return jwt.decode(
            token,
            signing_key,
            algorithms=_ASYMMETRIC_ALGS,
            audience='authenticated',
        )

    if alg == 'HS256':
        if not SUPABASE_JWT_SECRET:
            raise jwt.InvalidTokenError(
                'HS256 token received but SUPABASE_JWT_SECRET is not configured'
            )
        return jwt.decode(
            token,
            SUPABASE_JWT_SECRET,
            algorithms=['HS256'],
            audience='authenticated',
        )

    raise jwt.InvalidTokenError(f'Unsupported JWT algorithm: {alg}')


def get_current_user(
    creds: HTTPAuthorizationCredentials | None = Depends(_bearer_scheme),
) -> str:
    if creds is None or not creds.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Missing Authorization: Bearer <token> header',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    if not SUPABASE_URL and not SUPABASE_JWT_SECRET:
        logger.error('Neither SUPABASE_URL (for JWKS) nor SUPABASE_JWT_SECRET configured — cannot verify tokens')
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Auth not configured on the server',
        )

    try:
        payload = _verify_token(creds.credentials)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token expired — sign in again',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    except jwt.InvalidTokenError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'Invalid token: {exc}',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    except Exception as exc:
        # PyJWKClient can raise network errors fetching JWKS; surface them as 401
        # so a misconfigured backend doesn't look like a 500 to the user.
        logger.warning(f'JWT verification failed: {exc}')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'Token verification failed: {exc}',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    user_id = payload.get('sub')
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token missing subject claim',
        )
    return user_id



#This FastAPI authentication module validates the JWT access token sent by the Streamlit frontend. It extracts the Bearer token using FastAPI's HTTPBearer dependency, determines the JWT signing algorithm, and verifies the token either using Supabase's JWKS public key for asymmetric algorithms such as RS256/ES256 or using the Supabase JWT secret for HS256. After successful verification, it reads the sub claim from the payload to identify the authenticated user. If the token is missing, expired, invalid, or improperly configured, the API returns an appropriate HTTP error such as 401