
import json

from freelanceflow.core.schemas import Proposal, ProposalRequest
from freelanceflow.providers.openrouter import generate_text
from freelanceflow.services.pricing import calculate_estimate

SYSTEM_PROMPT = """Create a concise freelance proposal.
Return ONLY valid JSON with keys: title, summary, requirements,
assumptions, deliverables, exclusions, milestones, risks, client_email.
Use short strings and at most 2 items per list. No markdown fences.
Keep the response compact enough to fit 300 tokens."""


def create_proposal(request: ProposalRequest) -> Proposal:
    prompt = (
        f"Client: {request.client_name}\n"
        f"Brief: {request.project_brief}\n"
        "Create a concise proposal. Do not calculate price."
    )

    raw = generate_text(SYSTEM_PROMPT, prompt)
    try:
        data = json.loads(raw)
        data["estimated_cost"] = calculate_estimate(
            request.hourly_rate, request.estimated_hours
        )
        return Proposal.model_validate(data)
    except (json.JSONDecodeError, ValueError, TypeError) as exc:
        raise RuntimeError(
            "Invalid proposal response. Please try again."
        ) from exc
