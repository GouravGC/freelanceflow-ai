import os
from dotenv import load_dotenv
import sentry_sdk

load_dotenv()

dsn = os.getenv("SENTRY_DSN")
if not dsn:
    raise RuntimeError("SENTRY_DSN is missing from .env")

sentry_sdk.init(
    dsn=dsn,
    environment="development",
    send_default_pii=False,
)

sentry_sdk.capture_message(
    "FreelanceFlow AI - Sentry integration test",
    level="info",
)

sentry_sdk.flush(timeout=5)
print("Sentry test event sent. Check your Sentry dashboard.")