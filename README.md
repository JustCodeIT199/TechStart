# TechStart
TechStart is an AI-driven educational platform built using Django, FastAPI, and a fine-tuned Small Language Model (SLM). The system provides beginner-friendly topic explanations, quiz generation, and answer evaluation in multiple languages through an interactive web interface.
<div align="center">

<img src="https://img.shields.io/badge/TechStart-AI%20Learning%20Platform-4F46E5?style=for-the-badge&logo=graduation-cap&logoColor=white" alt="TechStart Banner" />

# TechStart : AI-Powered Learning Platform

**Multilingual intelligent tutoring powered by a fine-tuned Small Language Model**

[![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/)
[![CUDA](https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-toolkit)
[![License](https://img.shields.io/badge/License-Educational-blue?style=flat-square)](LICENSE)

</div>

---

## Overview

TechStart is an AI-driven educational platform built to democratize quality technical education. It uses a custom fine-tuned **Qwen 2.5 3B Small Language Model (SLM)** to deliver beginner-friendly explanations, dynamic quiz generation, and intelligent answer evaluation  all across multiple languages.

> Built as a Major Project for AI-powered multilingual education and intelligent tutoring systems.

---

## Features

### AI Tutor
- Structured, beginner-friendly concept explanations
- Step-by-step teaching methodology
- Real-life analogies and simplified breakdowns

### Quiz Generation
- Dynamic MCQ generation by topic
- Multi-language quiz support
- Contextually relevant questions

### Answer Evaluation
- Intelligent correctness feedback
- Detailed mistake explanations
- Improvement suggestions

### Multi-Language Support
| Language | Status |
|----------|--------|
| English  | Supported |
| Hindi    | Supported |
| Marathi  | Supported |

### Optimized AI Inference
- GPU-accelerated inference via NVIDIA CUDA
- CPU fallback support
- High-throughput response generation with FastAPI

---

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Frontend** | HTML, CSS, JavaScript, Bootstrap |
| **Backend** | Django, FastAPI, Uvicorn |
| **AI / ML** | PyTorch, Transformers, PEFT, Accelerate, Unsloth |
| **Database** | SQLite |
| **Auth** | Django Auth, Google OAuth |

---

## System Architecture

```
┌─────────────────────────────────────────────┐
│                    User                      │
└───────────────────┬─────────────────────────┘
                    │
┌───────────────────▼─────────────────────────┐
│           Django Frontend                    │
│         (Auth, UI, Sessions)                 │
└───────────────────┬─────────────────────────┘
                    │
┌───────────────────▼─────────────────────────┐
│           FastAPI AI Service                 │
│         (REST API · Port 8001)               │
└───────────────────┬─────────────────────────┘
                    │
┌───────────────────▼─────────────────────────┐
│         Fine-Tuned SLM (Qwen 2.5 3B)        │
│           LoRA · PEFT · Unsloth              │
└───────────────────┬─────────────────────────┘
                    │
┌───────────────────▼─────────────────────────┐
│            Generated Response                │
└─────────────────────────────────────────────┘
```

---

## AI / ML Highlights

- **Model**: Fine-tuned Qwen 2.5 3B using **LoRA** (Low-Rank Adaptation) via PEFT
- **Dataset**: Custom multilingual educational dataset (English, Hindi, Marathi)
- **Evaluation Metrics**: ROUGE Score, BLEU Score
- **Benchmark**: Fine-tuned model vs. base Qwen model comparison
- **Inference**: Optimized for GPU deployment; CPU fallback available

---

## Project Structure

```
TechStart/
│
├── frontend_django/          # Django web application
│   ├── templates/            # HTML templates
│   ├── static/               # CSS, JS, assets
│   ├── accounts/             # Auth (login, signup, OAuth)
│   └── manage.py
│
├── fastapi_slm/              # FastAPI AI inference service
│   ├── SLM_MERGED_v2/        # Fine-tuned model weights
│   ├── main.py               # API entrypoint
│   ├── requirements.txt
│   └── test_api.py
│
├── dataset/
│   ├── maindataset.json      # Training dataset
│   └── evaluation_dataset.json
│
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- (Optional) NVIDIA GPU with CUDA 12.1+

---

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd TechStart
```

---

### 2. Django Frontend Setup

```bash
# Create and activate virtual environment
python -m venv myenv
myenv\Scripts\activate        # Windows
# source myenv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Start the Django server
python manage.py runserver
```

> Frontend available at: `http://127.0.0.1:8000`

---

### 3. FastAPI AI Backend Setup

```bash
cd fastapi_slm

# Create and activate virtual environment
python -m venv myenv_3_11
myenv_3_11\Scripts\activate
```

**CPU Installation:**
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```

**NVIDIA GPU Installation (CUDA 12.1):**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

**Start the FastAPI server:**
```bash
uvicorn main:app --reload --port 8001
```

> AI backend available at: `http://127.0.0.1:8001`

---

## API Reference

### `POST /generate`

Generate a response from the AI tutor.

**Request Body:**

```json
{
  "mode": "teach",
  "topic": "Python Variables",
  "language": "English"
}
```

**Response:**

```json
{
  "response": "A variable in Python is used to store data..."
}
```

**Available Modes:**

| Mode    | Description                        |
|---------|------------------------------------|
| `teach` | Explains a concept step-by-step   |
| `quiz`  | Generates MCQ-based quiz questions |
| `grade` | Evaluates and scores user answers  |

---

## Model Evaluation

| Metric            | Base Qwen 2.5 3B | Fine-Tuned SLM |
|-------------------|-----------------|----------------|
| ROUGE Score       | Baseline         | Improved ✅     |
| BLEU Score        | Baseline         | Improved ✅     |
| Inference (CPU)   | 10–40 sec        | 10–40 sec      |
| Inference (GPU)   | 1–3 sec          | 1–3 sec        |

---

## Deployment

TechStart supports flexible deployment options:

- **Local**: Django on port 8000, FastAPI on port 8001
- **Remote Access**: [ngrok](https://ngrok.com/) for public tunneling
- **Hybrid**: Local frontend + remote GPU inference backend
- **Cloud GPU**: Deployable to any CUDA-compatible cloud instance

---

## Troubleshooting

<details>
<summary><strong>GPU not detected</strong></summary>

Verify CUDA availability:

```python
import torch
print(torch.cuda.is_available())  # Should return True
```

Ensure you installed the CUDA-specific PyTorch build.
</details>

<details>
<summary><strong>Slow responses</strong></summary>

| Hardware | Expected Response Time |
|----------|------------------------|
| CPU      | 10–40 seconds          |
| GPU      | 1–3 seconds            |

Consider switching to GPU inference for a production environment.
</details>

<details>
<summary><strong>Transformers / PEFT errors</strong></summary>

Perform a clean reinstall:

```bash
pip uninstall transformers peft accelerate -y
pip cache purge
pip install transformers peft accelerate
```
</details>

---

## Roadmap

- [ ] Voice-based AI tutor interaction
- [ ] Personalized learning path recommendations
- [ ] Cloud GPU deployment (AWS / GCP / Azure)
- [ ] Real-time speech interaction
- [ ] Student progress tracking & analytics dashboard
- [ ] Additional language support

---

## License

This project is intended for **educational and research purposes only**.

---
