
import streamlit as st

from freelanceflow.core.schemas import ProposalRequest
from freelanceflow.services.proposal_service import create_proposal

import os
import sentry_sdk
from dotenv import load_dotenv

load_dotenv()

sentry_dsn = os.getenv("SENTRY_DSN")

if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        environment=os.getenv("APP_ENV", "development"),
        send_default_pii=False,
    )

st.set_page_config(page_title="FreelanceFlow AI", page_icon="💼", layout="wide")

st.title("💼 FreelanceFlow AI")
st.caption("AI-powered freelance proposal copilot")

provider_options = {
    "OpenRouter (Cloud)": "openrouter",
    "Google Gemma (Local via Ollama)": "ollama",
}

with st.form("proposal_form"):
    provider_label = st.radio(
        "Choose inference provider",
        options=list(provider_options.keys()),
        horizontal=True,
    )

    client = st.text_input("Client name")
    brief = st.text_area("Project brief", height=180)
    col1, col2 = st.columns(2)

    with col1:
        rate = st.number_input("Hourly rate ($)", min_value=1.0, value=25.0)
    with col2:
        hours = st.number_input("Estimated hours", min_value=1.0, value=8.0)

    submitted = st.form_submit_button("Generate proposal")

if submitted:
    if not client.strip() or len(brief.strip()) < 20:
        st.error("Enter a client name and a brief of at least 20 characters.")
    else:
        try:
            request = ProposalRequest(
                client_name=client.strip(),
                project_brief=brief.strip(),
                hourly_rate=rate,
                estimated_hours=hours,
            )

            selected_provider = provider_options[provider_label]

            with st.spinner(f"Generating proposal using {provider_label}..."):
                proposal = create_proposal(request, provider=selected_provider)

            st.success(f"Proposal generated using {provider_label}!")
            st.subheader(proposal.title)
            st.write(proposal.summary)
            st.metric("Estimated cost", f"${proposal.estimated_cost:,.2f}")

            for section in (
                "requirements", "assumptions", "deliverables",
                "exclusions", "milestones", "risks",
            ):
                st.subheader(section.replace("_", " ").title())
                st.write(getattr(proposal, section))

            st.subheader("Client email")
            st.text_area("Email draft", proposal.client_email, height=180)

            st.download_button(
                "Download proposal (JSON)",
                proposal.model_dump_json(indent=2),
                file_name="freelance_proposal.json",
                mime="application/json",
            )
        except Exception as exc:
            st.error(str(exc))
