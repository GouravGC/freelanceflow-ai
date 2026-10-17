
from openai import OpenAI
from freelanceflow.core.config import settings


def generate_text(system_prompt: str, user_prompt: str) -> str:
    client = OpenAI(
        api_key="ollama",
        base_url=settings.OLLAMA_BASE_URL,
    )

    try:
        response = client.chat.completions.create(
            model=settings.OLLAMA_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=400,
            temperature=0.0,
            response_format={"type": "json_object"},
        )
    except Exception as exc:
        raise RuntimeError(
            "Could not generate a response from local Gemma. "
            "Check that Ollama is running and the model is installed."
        ) from exc

    return response.choices[0].message.content or ""
