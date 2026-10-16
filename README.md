# 🌉 SkillBridge AI – ATS Resume Analysis & Job Matching Platform

> An AI-powered platform that analyzes resumes against ATS standards, scores them against job descriptions, matches candidates to relevant roles, and generates downloadable PDF reports.


---

## 📌 Overview

**SkillBridge AI** helps job seekers see how their resume performs in ATS screening and which jobs fit their skills best. It parses uploaded resumes, extracts structured information with NLP, compares it with job descriptions using semantic similarity, and uses an LLM to produce clear, actionable feedback.

## ✨ Features

- 📄 **Resume Parsing**: Extracts text and details from PDF and DOCX files
- 🎯 **ATS Score**: Compatibility score between a resume and a job description
- 🔍 **Skill & Keyword Matching**: Fuzzy and semantic matching to find matched and missing skills
- 🧠 **Semantic Job Matching**: Sentence embeddings rank the best-fit roles
- 💡 **AI Suggestions**: LLM-powered (Groq) resume improvement tips
- 📑 **PDF Reports**: Downloadable analysis report
- 🔐 **User Authentication**: Email/password and OAuth login via Supabase
- 🔒 **Secure API**: Supabase JWT verification on backend endpoints

## 🏗️ Architecture

```
┌──────────────┐    REST     ┌──────────────────┐     ┌────────────┐
│  Streamlit   │ ──────────► │  FastAPI Backend │ ──► │  Supabase  │
│  Frontend    │ ◄────────── │  (NLP + ML)      │     │  (DB/Auth) │
└──────────────┘             └────────┬─────────┘     └────────────┘
                                      │
                         ┌────────────┴────────────┐
                         │ spaCy · Sentence-       │
                         │ Transformers · Groq LLM │
                         └─────────────────────────┘
```

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Frontend** | Streamlit, Requests, Supabase client |
| **Backend** | FastAPI, Uvicorn, Pydantic, python-dotenv |
| **NLP / ML** | spaCy (`en_core_web_md`), Sentence-Transformers, RapidFuzz, NumPy |
| **LLM** | Groq API |
| **File Parsing** | pdfplumber, PyPDF2, python-docx, python-magic |
| **Reports** | Jinja2, WeasyPrint |
| **Auth & Database** | Supabase (PyJWT, httpx REST client) |

## 📂 Project Structure

```
SkillBridgeAI/
│
├── .devcontainer/
│   └── devcontainer.json      # Dev container / Codespaces config
│
├── backend/
│   ├── api/                   # API routes
│   ├── core/                  # Config, security, app settings
│   ├── database/              # Supabase / database access layer
│   ├── logs/                  # Application logs
│   ├── models/                # Pydantic schemas / data models
│   ├── services/              # Parsing, scoring, matching, LLM, reports
│   ├── templates/             # Jinja2 templates for PDF reports
│   ├── utils/                 # Helper functions
│   └── main.py                # FastAPI entry point
│
├── frontend/
│   ├── components/            # Reusable UI components
│   ├── services/              # API client / auth helpers
│   ├── views/                 # App pages
│   └── streamlit_app.py       # Streamlit entry point
│
├── models/                    # Local sentence-transformer model files
│   ├── 1_Pooling/
│   ├── config.json
│   ├── modules.json
│   ├── tokenizer.json
│   └── ...
│
├── .gitignore
├── requirements.txt
├── runtime.txt                # Python version for deployment
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A [Supabase](https://supabase.com) project (auth and database)
- A [Groq](https://console.groq.com) API key
- System libraries for file handling and PDF generation (see below)

### System Dependencies

**Ubuntu / Debian**
```bash
sudo apt-get install libmagic1 libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b
```

**macOS**
```bash
brew install libmagic pango
```

**Windows**
- `python-magic`: `pip install python-magic-bin`
- WeasyPrint: follow the [official install guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html)

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/ISHI-456/SkillBridgeAI-ATS-Resume-Analysis-and-Job-Matching-Platform.git
   cd SkillBridgeAI-ATS-Resume-Analysis-and-Job-Matching-Platform
```

2. **Create and activate a virtual environment**
```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```
   > The spaCy `en_core_web_md` model is installed automatically from the wheel URL at the end of `requirements.txt`. If that step fails, run `python -m spacy download en_core_web_md`.

### Environment Variables

Create a `.env` file in the project root:

```env
# Supabase
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
SUPABASE_JWT_SECRET=your_supabase_jwt_secret

# Groq
GROQ_API_KEY=your_groq_api_key

# App
BACKEND_URL=http://localhost:8000
```

> ⚠️ Never commit your `.env` file. Make sure it is listed in `.gitignore`.

### Running the App

**1. Start the backend (FastAPI)**
```bash
uvicorn backend.main:app --reload --port 8000
```
Interactive API docs: `http://localhost:8000/docs`

**2. Start the frontend (Streamlit)** in a new terminal
```bash
streamlit run frontend/streamlit_app.py
```
Open `http://localhost:8501` in your browser.

## 🧑‍💻 How to Use

1. **Sign up / log in** with email or OAuth
2. **Upload your resume** (PDF or DOCX)
3. **Paste a job description** or choose a target role
4. Click **Analyze** to get your ATS score, skill gaps, and AI suggestions
5. Browse **matching jobs** ranked by fit
6. **Download the PDF report**

## 🔌 API Documentation

With the backend running, visit `http://localhost:8000/docs` (Swagger UI) or `http://localhost:8000/redoc` for all endpoints.



## 🔮 Future Enhancements

- [ ] Live job feeds (LinkedIn / Indeed APIs)
- [ ] AI resume rewriting
- [ ] Multi-language support
- [ ] Cover letter generator
- [ ] Docker support

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request





---

⭐ If you find this project useful, consider giving it a star!
