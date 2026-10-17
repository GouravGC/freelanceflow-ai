# FreelanceFlow AI

**AI-powered freelance proposal copilot**

FreelanceFlow AI transforms a client's project brief into a structured freelance proposal using an LLM through OpenRouter.

## Features

- AI-generated project proposals
- Structured requirements, assumptions, deliverables, exclusions, milestones, and risks
- Estimated project pricing based on hourly rate and estimated hours
- Draft client email
- Download proposals as JSON
- Input validation with Pydantic
- Automated unit tests with pytest
- Modular Python architecture

## Technology Stack

- Python 3.11+
- Streamlit
- OpenRouter API
- OpenAI Python SDK
- Pydantic
- pytest
- Docker
- GitHub Actions

## Project Structure

```text
freelanceflow-ai/
├── app.py
├── src/freelanceflow/
│   ├── core/
│   ├── providers/
│   └── services/
├── tests/
├── docs/
├── examples/
├── .github/workflows/ci.yml
├── .env.example
├── Dockerfile
├── .dockerignore
└── requirements.txt
```

## Local Setup

1. Create and activate your Python environment.
2. Install dependencies:

   `python -m pip install -r requirements.txt`

3. Copy `.env.example` to `.env` and configure your OpenRouter API key and model.
4. Set the source path in Windows CMD:

   `set PYTHONPATH=src`

5. Start the application:

   `streamlit run app.py`

Open `http://localhost:8501`.

## Testing

```cmd
set PYTHONPATH=src
python -m pytest tests -v
```

## Configuration

Set `OPENROUTER_API_KEY` and `OPENROUTER_MODEL` in `.env`. Never commit API keys or other secrets.

## Pricing

The estimated project cost is calculated as:

`hourly_rate × estimated_hours`

## Security

Keep `.env` out of version control. Use environment variables or a secrets manager for deployment.

## Disclaimer

AI-generated proposals may contain inaccurate assumptions. Review all proposal details before sharing them with a client.