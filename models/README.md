---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:316
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-mpnet-base-v2
widget:
- source_sentence: 'Financial Analyst | around 1 years working in the industry

    - Proficient in Accounting

    - Proficient in Budgeting

    - Proficient in Valuation

    - Proficient in Variance Analysis

    - Collaborated closely with stakeholders to translate requirements into solutions.'
  sentences:
  - 'Job Title: Financial Analyst

    We need someone with at least 1 years of relevant experience and hands-on expertise
    in PowerPoint, Financial Modeling, SQL, and Forecasting. Day-to-day work: improving
    existing systems and processes for reliability and performance.'
  - 'Job Title: HR Specialist

    We need someone with at least 1 years of relevant experience and hands-on expertise
    in Recruiting, Conflict Resolution, Onboarding, and Compliance. Day-to-day work:
    partnering with stakeholders to define priorities and deliver measurable outcomes.'
  - Our company is looking for an experienced financial analyst (7+ years) who is
    proficient in Forecasting, PowerPoint, and SQL, and ideally also SAP. The role
    involves improving existing systems and processes for reliability and performance.
- source_sentence: Full Stack Developer with over 5 years of hands-on experience.
    Skilled in React, Git, JavaScript, Express.js, and Node.js. Known for strong problem-solving
    and attention to detail.
  sentences:
  - 'Job Title: Full Stack Developer

    We need someone with at least 4 years of relevant experience and hands-on expertise
    in HTML, REST APIs, React, Node.js, JavaScript, and Express.js. Day-to-day work:
    mentoring junior team members while contributing hands-on to key initiatives.'
  - 'Job Title: DevOps Engineer

    We need someone with at least 2 years of relevant experience and hands-on expertise
    in AWS, Terraform, Ansible, Bash Scripting, and CI/CD. Day-to-day work: owning
    projects end-to-end, from requirements gathering to delivery and support.'
  - 'Job Title: Marketing Manager

    We need someone with at least 2 years of relevant experience and hands-on expertise
    in Social Media, SEO, Email Marketing, and PPC. Day-to-day work: mentoring junior
    team members while contributing hands-on to key initiatives.'
- source_sentence: QA Engineer with over 10 years of hands-on experience. Skilled
    in Postman, Test Automation, Jira, Selenium, TestNG, and Manual Testing. Received
    recognition for improving process efficiency.
  sentences:
  - 'Job Title: Software Engineer

    We need someone with at least 8 years of relevant experience and hands-on expertise
    in Agile, Docker, Git, and Python. Day-to-day work: troubleshooting production
    issues and maintaining clear documentation.'
  - 'Marketing Manager Opening

    Experience required: 3+ years

    Must-have skills: PPC, Social Media, Campaign Management, Email Marketing

    You will: improving existing systems and processes for reliability and performance'
  - 'Job Title: QA Engineer

    We need someone with at least 9 years of relevant experience and hands-on expertise
    in TestNG, Selenium, CI/CD, Java, and Manual Testing. Day-to-day work: designing
    and implementing scalable solutions while collaborating with cross-functional
    teams.'
- source_sentence: Cloud Engineer with over 1 years of hands-on experience. Skilled
    in CI/CD, Terraform, AWS, Cloud Security, Networking, and GCP. Known for strong
    problem-solving and attention to detail.
  sentences:
  - 'Healthcare Data Analyst Opening

    Experience required: 1+ years

    Must-have skills: Statistics, SQL, Power BI, Python

    You will: partnering with stakeholders to define priorities and deliver measurable
    outcomes'
  - Our company is looking for an experienced software engineer (10+ years) who is
    proficient in Docker, Git, and REST APIs, and ideally also Data Structures, Unit
    Testing. The role involves troubleshooting production issues and maintaining clear
    documentation.
  - Our company is looking for an experienced cloud engineer (5+ years) who is proficient
    in CI/CD, Azure, and Terraform, and ideally also Cloud Security, GCP. The role
    involves partnering with stakeholders to define priorities and deliver measurable
    outcomes.
- source_sentence: 'DevOps Engineer | 3 years of experience

    - Proficient in Jenkins

    - Proficient in AWS

    - Proficient in Terraform

    - Proficient in Docker

    - Strong communicator with experience presenting to non-technical audiences.'
  sentences:
  - Our company is looking for an experienced data scientist (5+ years) who is proficient
    in A/B Testing, SQL, and Machine Learning, and ideally also Data Visualization,
    Deep Learning. The role involves troubleshooting production issues and maintaining
    clear documentation.
  - 'DevOps Engineer Opening

    Experience required: 1+ years

    Must-have skills: Jenkins, Kubernetes, AWS, Terraform

    You will: designing and implementing scalable solutions while collaborating with
    cross-functional teams'
  - 'UX Designer Opening

    Experience required: 10+ years

    Must-have skills: Prototyping, Adobe XD, Sketch, Usability Testing, Wireframing

    You will: troubleshooting production issues and maintaining clear documentation'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
model-index:
- name: SentenceTransformer based on sentence-transformers/all-mpnet-base-v2
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: ats val
      type: ats-val
    metrics:
    - type: pearson_cosine
      value: 0.8289797581622623
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.7728724853495117
      name: Spearman Cosine
---

# SentenceTransformer based on sentence-transformers/all-mpnet-base-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) <!-- at revision e8c3b32edf5434bc2275fc9bab85f82640a19130 -->
- **Maximum Sequence Length:** 384 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'MPNetModel'})
  (1): Pooling({'embedding_dimension': 768, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'DevOps Engineer | 3 years of experience\n- Proficient in Jenkins\n- Proficient in AWS\n- Proficient in Terraform\n- Proficient in Docker\n- Strong communicator with experience presenting to non-technical audiences.',
    'DevOps Engineer Opening\nExperience required: 1+ years\nMust-have skills: Jenkins, Kubernetes, AWS, Terraform\nYou will: designing and implementing scalable solutions while collaborating with cross-functional teams',
    'Our company is looking for an experienced data scientist (5+ years) who is proficient in A/B Testing, SQL, and Machine Learning, and ideally also Data Visualization, Deep Learning. The role involves troubleshooting production issues and maintaining clear documentation.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.8789, 0.2689],
#         [0.8789, 1.0000, 0.2418],
#         [0.2689, 0.2418, 1.0000]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Semantic Similarity

* Dataset: `ats-val`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.sentence_transformer.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.829      |
| **spearman_cosine** | **0.7729** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 316 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                         | sentence_1                                                                         | label                                                            |
  |:---------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------|
  | type     | string                                                                             | string                                                                             | float                                                            |
  | modality | text                                                                               | text                                                                               |                                                                  |
  | details  | <ul><li>min: 35 tokens</li><li>mean: 44.46 tokens</li><li>max: 54 tokens</li></ul> | <ul><li>min: 38 tokens</li><li>mean: 53.63 tokens</li><li>max: 69 tokens</li></ul> | <ul><li>min: 0.05</li><li>mean: 0.56</li><li>max: 0.99</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                              | sentence_1                                                                                                                                                                                                                                                                                      | label             |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
  | <code>Results-driven systems administrator (3 years of professional experience). Core skills: PowerShell, Backup Solutions, Active Directory, Bash Scripting, Networking, Monitoring. Strong communicator with experience presenting to non-technical audiences.</code> | <code>Job Title: Full Stack Developer<br>We need someone with at least 1 years of relevant experience and hands-on expertise in Node.js, JavaScript, MongoDB, and React. Day-to-day work: owning projects end-to-end, from requirements gathering to delivery and support.</code>               | <code>0.09</code> |
  | <code>Software Engineer with around 11 years working in the industry. Skilled in Python, REST APIs, Data Structures, and Docker. Collaborated closely with stakeholders to translate requirements into solutions.</code>                                                | <code>We are hiring a Software Engineer to join our growing team. Requirements: 9+ years of experience and strong knowledge of Java, Data Structures, Python, Docker, and SQL. Responsibilities include owning projects end-to-end, from requirements gathering to delivery and support.</code> | <code>0.95</code> |
  | <code>Machine Learning Engineer with around 8 years working in the industry. Skilled in Kubernetes, Scikit-learn, PyTorch, and AWS. Passionate about continuous learning and staying current with industry trends.</code>                                               | <code>Job Title: Machine Learning Engineer<br>We need someone with at least 8 years of relevant experience and hands-on expertise in Python, PyTorch, AWS, MLOps, and Kubernetes. Day-to-day work: improving existing systems and processes for reliability and performance.</code>             | <code>0.84</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss",
      "cos_score_transformation": "torch.nn.modules.linear.Identity"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 16
- `num_train_epochs`: 5
- `fp16`: True
- `per_device_eval_batch_size`: 16
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 16
- `num_train_epochs`: 5
- `max_steps`: -1
- `learning_rate`: 5e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: True
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 16
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `dataloader_multiprocessing_context`: None
- `dataloader_in_order`: True
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}
- `warmup_ratio`: None

</details>

### Training Logs
| Epoch | Step | ats-val_spearman_cosine |
|:-----:|:----:|:-----------------------:|
| 1.0   | 20   | 0.7591                  |
| 2.0   | 40   | 0.7729                  |


### Training Time
- **Training**: 50.1 seconds

### Framework Versions
- Python: 3.13.15
- Sentence Transformers: 5.7.0
- Transformers: 5.15.0
- PyTorch: 2.11.0+cu128
- Accelerate: 1.14.0
- Datasets: 4.0.0
- Tokenizers: 0.22.2

## Additional Resources

- [Training and Finetuning Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-sentence-transformers): the end-to-end guide for training or finetuning Sentence Transformer models.
- [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka): variable-size embeddings that can be truncated with minimal quality loss.
- [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): train multimodal embedding models, with a Visual Document Retrieval walkthrough.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->