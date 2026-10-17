# FreelanceFlow AI 🚀

**AI-powered freelance proposal copilot** that turns a client's brief into a structured proposal with pricing, scope, milestones, risks, and a client-ready email.

<p align="left">
  <a href="https://freelanceflow-ai-2du9.onrender.com/">🌐 Live Demo</a> ·
  <a href="https://github.com/GouravGC/freelanceflow-ai">📦 Source Code</a> ·
  <a href="https://github.com/GouravGC/freelanceflow-ai/pkgs/container/freelanceflow-ai">🐳 Docker Image</a> ·
  <a href="https://gouravgc.sentry.io/issues/?project=-1&statsPeriod=14d">🛡️ Sentry Dashboard</a>
</p>

[![CI and Docker Publish](https://github.com/GouravGC/freelanceflow-ai/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GouravGC/freelanceflow-ai/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED)

> **Status:** Deployed on Render. OpenRouter proposal generation has been tested successfully. Sentry event delivery has been verified locally; production monitoring still needs verification.

## Features

- Generate proposals from plain-language project briefs.
- Choose OpenRouter cloud inference or Google Gemma through local Ollama.
- Produce structured sections: requirements, assumptions, deliverables, exclusions, milestones, and risks.
- Estimate cost using hourly rate × estimated hours.
- Generate a client-ready email draft.
- Download generated proposal data as JSON.
- Validate inputs and proposal data with Pydantic.
- Modular Python code structure.
- Automated tests with pytest.
- Docker image publishing to GitHub Container Registry (GHCR).
- GitHub Actions workflow for testing and image publishing.
- Sentry SDK integration, when configured correctly in the running deployment.

## Project Links

| Resource | Link |
|---|---|
| Live application | https://freelanceflow-ai-2du9.onrender.com/ |
| GitHub repository | https://github.com/GouravGC/freelanceflow-ai |
| Docker package | https://github.com/GouravGC/freelanceflow-ai/pkgs/container/freelanceflow-ai |
| GitHub Actions run | https://github.com/GouravGC/freelanceflow-ai/actions/runs/39009810226 |
| Sentry dashboard | https://gouravgc.sentry.io/issues/?project=-1&statsPeriod=14d |

The Sentry link may require signing in to the correct organization and selecting the `freelanceflow-ai` project.

## Technology Stack

- Python 3.11+
- Streamlit
- OpenRouter API for cloud inference
- Google Gemma via Ollama for local inference
- Pydantic for validation
- pytest for tests
- Sentry Python SDK for monitoring
- Docker and GitHub Container Registry
- GitHub Actions for CI and image publishing
- Render for hosting

## Architecture

```text
Client brief + pricing inputs
            |
            v
      Streamlit UI (app.py)
            |
            v
     Proposal generation service
            |
            +----------------------+
            |                      |
            v                      v
    OpenRouter provider      Local Ollama provider
            |                      |
            +----------+-----------+
                       |
                       v
             Structured proposal
                       |
          +------------+------------+
          |            |            |
          v            v            v
      UI display    Email draft   JSON download

GitHub push -> GitHub Actions -> tests -> Docker build -> GHCR
                                                   |
                                     Render deploy (manual or hook)
```

## Try the Live Demo

1. Open the [live app](https://freelanceflow-ai-2du9.onrender.com/).
2. Choose **OpenRouter (Cloud)** on the hosted app.
3. Enter the client name and project brief.
4. Enter the hourly rate and estimated hours.
5. Generate and review the proposal.
6. Download the proposal JSON if needed.

Example: `$30/hour × 60 hours = $1,800`.

> The local Ollama option requires Ollama and a compatible model running on your machine. It is not available on Render unless separately hosted and configured.

## Local Setup

### Prerequisites

- Python 3.11+
- Git
- An OpenRouter API key for cloud inference
- Optional: [Ollama](https://ollama.com/) and a compatible Gemma model

### 1. Clone the repository

```bash
git clone https://github.com/GouravGC/freelanceflow-ai.git
cd freelanceflow-ai
```

### 2. Create and activate a Conda environment (Windows CMD)

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

Copy `.env.example` to `.env`, then fill in the values required by your chosen provider.

Example `.env`:

```dotenv
AI_PROVIDER=openrouter
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL=openrouter/free
APP_ENV=development
SENTRY_DSN=
```

Use the exact variable names expected by the current app and `.env.example`. Never commit `.env` or publish API keys, credentials, or secret values.

### 5. Run the app

```cmd
set PYTHONPATH=src
streamlit run app.py
```

Open http://localhost:8501.

## Run Tests

From the project root in Windows CMD:

```cmd
set PYTHONPATH=src
python -m pytest tests -v
```

The test suite previously passed six tests. Run it against your current checkout to verify the latest state.

## Docker

Published image:

`ghcr.io/gouravgc/freelanceflow-ai:latest`

Pull the image:

```bash
docker pull ghcr.io/gouravgc/freelanceflow-ai:latest
```

Run it locally (provide your own key):

```bash
docker run --rm -p 8501:8501 \
  -e AI_PROVIDER=openrouter \
  -e OPENROUTER_API_KEY=your_openrouter_api_key \
  -e OPENROUTER_MODEL=openrouter/free \
  -e APP_ENV=production \
  ghcr.io/gouravgc/freelanceflow-ai:latest
```

Do not put real secrets in commands committed to Git or in public documentation.

## CI/CD and Deployment

The workflow lives at `.github/workflows/ci.yml`. It runs tests and, on pushes to `main`, builds and publishes a Docker image to GHCR.

- [GitHub Actions workflow run](https://github.com/GouravGC/freelanceflow-ai/actions/runs/39009810226)
- [GHCR package](https://github.com/GouravGC/freelanceflow-ai/pkgs/container/freelanceflow-ai)
- [Render app](https://freelanceflow-ai-2du9.onrender.com/)

Render image-based services may not redeploy automatically when a mutable `latest` tag changes. For automatic deployment, create a Render Deploy Hook, save its URL as the GitHub Actions secret `RENDER_DEPLOY_HOOK_URL`, and call it after the Docker image push. Otherwise, manually deploy the latest image from Render and verify the deployment in its Events/Deploys page.

Keep production API keys and `SENTRY_DSN` in Render environment settings. Add GitHub Actions secrets only when a workflow needs them.

## Sentry Monitoring

Sentry SDK integration is intended to capture application events and exceptions when a valid `SENTRY_DSN` is configured.

- [Open Sentry dashboard](https://gouravgc.sentry.io/issues/?project=-1&statsPeriod=14d)
- Set `SENTRY_DSN` locally and in Render.
- Set `APP_ENV=production` in Render.
- Ensure the deployed Docker image includes `sentry-sdk` and the Sentry initialization code.
- Verify events in the correct Sentry project and environment after deployment.

A successful local test proves local event delivery only; it does not confirm that production events are reaching Sentry.

## Pricing

The basic estimate is calculated as:

```text
estimated_cost = hourly_rate × estimated_hours
```

This is a planning estimate, not a binding quote. Review scope, assumptions, exclusions, and generated content before sending a proposal to a client.

## Project Structure

```text
freelanceflow-ai/
├── app.py
├── src/
│   └── freelanceflow/
│       ├── core/
│       ├── providers/
│       └── services/
├── tests/
├── docs/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .env.example
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

This is a high-level overview; consult the repository for the complete current structure.

## Security Notes

- Never commit `.env`, API keys, credentials, or deployment secrets.
- Store production configuration in Render environment variables.
- Review AI-generated content before sharing it with clients.
- Use payment sandbox credentials for any future payment integration.

## Roadmap

- [ ] Improve specificity of generated deliverables and milestones.
- [ ] Verify Sentry event delivery in production.
- [ ] Finish automatic Render deployment after GHCR image publishing.
- [ ] Add web/market research support.

## License

See the repository's `LICENSE` file for license details.
