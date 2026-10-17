from pydantic import BaseModel, Field


class ProposalRequest(BaseModel):
    client_name: str = Field(min_length=1, max_length=120)
    project_brief: str = Field(min_length=20, max_length=8000)
    hourly_rate: float = Field(gt=0, le=10000)
    estimated_hours: float = Field(gt=0, le=10000)


class Proposal(BaseModel):
    title: str
    summary: str
    requirements: list[str]
    assumptions: list[str]
    deliverables: list[str]
    exclusions: list[str]
    milestones: list[str]
    risks: list[str]
    client_email: str
    estimated_cost: float