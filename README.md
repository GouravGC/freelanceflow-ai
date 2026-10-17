# FreelanceFlow AI 🚀

**An AI-powered freelance proposal copilot** that transforms client project briefs into structured proposals with pricing, requirements, assumptions, deliverables, milestones, risks, and a client-ready email.

## 🎥 Project Demo

Watch the FreelanceFlow AI walkthrough on YouTube:

[![FreelanceFlow AI Demo](https://img.youtube.com/vi/0vEj6Pujp5Y/maxresdefault.jpg)](https://www.youtube.com/watch?v=0vEj6Pujp5Y)

▶️ **[Watch the full demo on YouTube](https://www.youtube.com/watch?v=0vEj6Pujp5Y)**

🌐 **[Try the live application](https://freelanceflow-ai-2du9.onrender.com/)**

## 🔎 Project Evidence

**[📸 View All Project Evidence](https://github.com/GouravGC/freelanceflow-ai/tree/main/evidences)**

Explore the evidence folder for screenshots and supporting material demonstrating the project.

## 🔗 Important Links

| Resource | Link |
|---|---|
| 🌐 Live Application | [FreelanceFlow AI](https://freelanceflow-ai-2du9.onrender.com/) |
| 📸 **Project Evidence** | [Evidence Folder](https://github.com/GouravGC/freelanceflow-ai/tree/main/evidences) |
| 📦 Source Code | [GitHub Repository](https://github.com/GouravGC/freelanceflow-ai) |
| 🧩 Modular Source | [src/freelanceflow](https://github.com/GouravGC/freelanceflow-ai/tree/main/src/freelanceflow) |
| 🧪 Automated Tests | [Tests Folder](https://github.com/GouravGC/freelanceflow-ai/tree/main/tests) |
| ⚙️ CI/CD Workflow | [GitHub Actions](https://github.com/GouravGC/freelanceflow-ai/actions/workflows/ci.yml) |
| ✅ Workflow Run | [View Recorded Run](https://github.com/GouravGC/freelanceflow-ai/actions/runs/39009810226) |
| 🐳 Docker Image | [GitHub Container Registry](https://github.com/GouravGC/freelanceflow-ai/pkgs/container/freelanceflow-ai) |
| 🛡️ Error Monitoring | [Sentry Dashboard](https://gouravgc.sentry.io/issues/?project=-1&statsPeriod=14d) |

The Sentry dashboard may require signing in and selecting the `freelanceflow-ai` project.

## 💡 Overview

Freelancers frequently spend time converting client briefs into clear project scopes, estimates, milestones, and professional proposals. FreelanceFlow AI streamlines this process by using a large language model to generate a structured proposal from natural-language input.

The application also calculates a project cost estimate from the hourly rate and estimated hours, helping freelancers prepare a consistent starting point for client discussions.

## ✨ Features

- AI-generated proposals from client project briefs.
- Two inference options: OpenRouter cloud inference and Google Gemma through local Ollama.
- Structured requirements, assumptions, deliverables, exclusions, milestones, and risks.
- Automatic cost estimation using hourly rate × estimated hours.
- Professional client email draft.
- JSON proposal download.
- Input and data validation with Pydantic.
- Modular Python architecture.
- Automated testing with pytest.
- Docker containerization and image publishing to GHCR.
- GitHub Actions workflow for automated tests and container publishing.
- Sentry SDK integration for application monitoring when correctly configured.

## 🧰 Technology Stack

- **Language:** Python 3.11+
- **Frontend:** Streamlit
- **Cloud inference:** OpenRouter API
- **Local inference:** Google Gemma via Ollama
- **Validation:** Pydantic
- **Testing:** pytest
- **Monitoring:** Sentry Python SDK
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Container registry:** GitHub Container Registry (GHCR)
- **Deployment:** Render

## 🏗️ Architecture

```text
Client Brief + Pricing Inputs
             |
             v
       Streamlit Frontend
             |
             v
    Proposal Generation Service
             |
       +-----+------+
       |            |
       v            v
   OpenRouter    Local Ollama
   (Cloud)       (Gemma Model)
       |            |
       +-----+------+
             |
             v
     Structured Proposal
             |
      +------+------+------+
      |             |      |
      v             v      v
   Display      Email Draft JSON Download

GitHub Push -> GitHub Actions -> Tests
                                  |
                                  v
                           Docker Build
                                  |
                                  v
                                 GHCR
                                  |
                                  v
                          Render Deployment
```

## 🚀 Try the Live Demo

1. Open the [live application](https://freelanceflow-ai-2du9.onrender.com/).
2. Select **OpenRouter (Cloud)** for the hosted demo.
3. Enter a client name and project brief.
4. Provide an hourly rate and estimated hours.
5. Generate and review the proposal.
6. Download the proposal as JSON.

### Example

- **Client:** NovaStyle Fashion
- **Project:** Responsive e-commerce website with product listings, filters, product pages, cart, sandbox checkout, user accounts, order confirmation emails, and an admin dashboard.
- **Hourly rate:** $30
- **Estimated hours:** 60
- **Estimated cost:** $1,800

The estimate is calculated as:

`estimated_cost = hourly_rate × estimated_hours`

This is a planning estimate, not a binding quote. Review the generated scope, assumptions, exclusions, and other details before sharing a proposal.

> **Local inference:** The Ollama/Gemma option requires Ollama and a compatible model running on the local machine. It is not available on Render unless a separate inference service is configured.

## 🛠️ Local Setup (Windows CMD)

### Prerequisites

- Python 3.11+
- Git
- OpenRouter API key for cloud inference
- Optional: [Ollama](https://ollama.com/) and a compatible Gemma model

### 1. Clone the repository

```cmd
git clone https://github.com/GouravGC/freelanceflow-ai.git
cd freelanceflow-ai
```

### 2. Create and activate the Conda environment

```cmd
conda create -n hacktoberfest2 python=3.11 -y
conda activate hacktoberfest2
```

If the environment already exists, activate it instead of recreating it.

### 3. Install dependencies

```cmd
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and fill in the values required by your selected provider.

Example:

```dotenv
AI_PROVIDER=openrouter
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL=openrouter/free
APP_ENV=development
SENTRY_DSN=
```

Use the exact variable names expected by the application and `.env.example`. **Never commit `.env`, API keys, credentials, or other secrets.**

### 5. Run the application

```cmd
set PYTHONPATH=src
streamlit run app.py
```

Open `http://localhost:8501`.

## 🧪 Run Automated Tests

From the repository root:

```cmd
set PYTHONPATH=src
python -m pytest tests -v
```

## 🐳 Docker

Published image:

`ghcr.io/gouravgc/freelanceflow-ai:latest`

Pull the image:

```cmd
docker pull ghcr.io/gouravgc/freelanceflow-ai:latest
```

Run locally with your own API key:

```cmd
docker run --rm -p 8501:8501 -e AI_PROVIDER=openrouter -e OPENROUTER_API_KEY=your_openrouter_api_key -e OPENROUTER_MODEL=openrouter/free -e APP_ENV=production ghcr.io/gouravgc/freelanceflow-ai:latest
```

Do not publish real secrets in commands, documentation, or source control.

## ⚙️ CI/CD and Deployment

The workflow is located at `.github/workflows/ci.yml`. It runs automated tests and publishes a Docker image to GHCR when configured push conditions are met.

- [Workflow definition](https://github.com/GouravGC/freelanceflow-ai/actions/workflows/ci.yml)
- [Referenced workflow run](https://github.com/GouravGC/freelanceflow-ai/actions/runs/39009810226)
- [Published container package](https://github.com/GouravGC/freelanceflow-ai/pkgs/container/freelanceflow-ai)
- [Live application](https://freelanceflow-ai-2du9.onrender.com/)

Publishing a new `latest` image does not necessarily trigger a Render deployment automatically. Depending on the service configuration, a manual deploy or configured Render Deploy Hook may be required. Check the deployment status in Render before assuming the newest image is live.

## 🛡️ Sentry Monitoring

Sentry integration is included for application monitoring when configured correctly.

- [Sentry dashboard](https://gouravgc.sentry.io/issues/?project=-1&statsPeriod=14d)
- Configure `SENTRY_DSN` in the local environment and Render.
- Set `APP_ENV=production` in Render.
- Ensure the deployed image includes `sentry-sdk` and the initialization code.
- Verify events in the correct Sentry project and environment.

A successful local test confirms local event delivery only; production event delivery must be verified separately.

## 🔐 Security and Responsible Use

- Keep `.env`, API keys, and deployment secrets out of Git.
- Use environment variables or an appropriate secrets manager for production configuration.
- Review AI-generated proposals for accuracy and feasibility before sending them to clients.
- Treat cost estimates as planning guidance, not guaranteed quotes.

## 📁 Project Structure

```text
freelanceflow-ai/
├── app.py
├── src/
│   └── freelanceflow/
│       ├── core/
│       ├── providers/
│       └── services/
├── tests/
├── evidences/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .env.example
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

This is a high-level overview. See the repository for the complete current structure.

## 🗺️ Future Improvements

- Improve the specificity of generated deliverables and milestones.
- Verify Sentry event delivery in production.
- Confirm automatic Render deployment after GHCR publishing.
- Explore optional web and market research support.

## 📄 License

Refer to the repository's `LICENSE` file for licensing terms. If no license file exists, clarify the intended license before describing the project as open source.
