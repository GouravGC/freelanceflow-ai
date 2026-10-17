
from openai import OpenAI
from freelanceflow.core.config import settings


def generate_text(system_prompt: str, user_prompt: str) -> str:
    if not settings.OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY missing in .env")

    if not settings.OPENROUTER_MODEL:
        raise RuntimeError("OPENROUTER_MODEL missing in .env")

    client = OpenAI(
        api_key=settings.OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )

    response = client.chat.completions.create(
        model=settings.OPENROUTER_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=700,
        temperature=0.2,
    )

    return response.choices[0].message.content or ""
