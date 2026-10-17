
from freelanceflow.core.config import settings
from freelanceflow.core.schemas import Proposal, ProposalRequest
from freelanceflow.providers.openrouter import generate_text as generate_openrouter
from freelanceflow.providers.ollama import generate_text as generate_ollama
from freelanceflow.services.pricing import calculate_estimate


SYSTEM_PROMPT = """Create a concise freelance proposal.
Return exactly two lines:
TITLE: a short proposal title
SUMMARY: a one-sentence project summary
No JSON, lists, markdown, or extra text.
Keep the entire response under 70 tokens."""


def create_proposal(
    request: ProposalRequest,
    provider: str | None = None,
) -> Proposal:
    selected_provider = (provider or settings.AI_PROVIDER).strip().lower()

    prompt = (
        f"Client: {request.client_name}\n"
        f"Project brief: {request.project_brief}\n"
        "Write a suitable title and one-sentence summary."
    )

    if selected_provider == "openrouter":
        generate = generate_openrouter
    elif selected_provider == "ollama":
        generate = generate_ollama
    else:
        raise ValueError(f"Unsupported AI provider: {selected_provider}")

    # Reliable defaults ensure the proposal remains valid even if
    # a small model returns empty or unusable text.
    title = f"{request.client_name} - Project Proposal"
    summary = (
        f"A proposal for {request.client_name} based on the "
        f"following brief: {request.project_brief}"
    )

    try:
        raw = generate(SYSTEM_PROMPT, prompt)
    except Exception:
        raw = ""

    if raw and raw.strip():
        lines = raw.strip().splitlines()
        generated_title = ""
        generated_summary = []

        for line in lines:
            cleaned = line.strip()
            upper = cleaned.upper()

            if upper.startswith("TITLE:"):
                generated_title = cleaned.split(":", 1)[1].strip()
            elif upper.startswith("SUMMARY:"):
                generated_summary.append(
                    cleaned.split(":", 1)[1].strip()
                )
            elif generated_summary:
                generated_summary.append(cleaned)

        if generated_title:
            title = generated_title[:200]

        if generated_summary:
            candidate = " ".join(generated_summary).strip()
            if candidate:
                summary = candidate[:1000]

    estimated_cost = calculate_estimate(
        request.hourly_rate,
        request.estimated_hours,
    )

    return Proposal(
        title=title,
        summary=summary,
        requirements=[request.project_brief],
        assumptions=[
            "Client will provide required content and branding assets."
        ],
        deliverables=[
            "Project implementation based on the agreed requirements."
        ],
        exclusions=[
            "Ongoing maintenance and additional paid services unless agreed."
        ],
        milestones=[
            "Requirements approval, implementation, testing, and handover."
        ],
        risks=[
            "Scope changes or delayed client inputs may affect delivery."
        ],
        client_email=(
            f"Hi {request.client_name},\n\n"
            f"Thank you for sharing your project requirements. "
            f"We propose delivering the project described here: "
            f"{request.project_brief}\n\n"
            f"The estimated project cost is ${estimated_cost:,.2f}. "
            "Please let me know if you would like to discuss the scope "
            "and next steps.\n\nBest regards"
        ),
        estimated_cost=estimated_cost,
    )
