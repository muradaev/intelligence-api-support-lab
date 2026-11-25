# Intelligence API — Support Incident Lab

A hands-on API troubleshooting lab simulating support incidents in a B2B intelligence data platform.

## Features

- Organization search with API key authentication
- HTTP 401 authentication failures
- Missing data and provider outages (HTTP 503)
- Upstream rate limiting (HTTP 429)
- Request ID correlation and server logging
- Automated Postman tests and Python diagnostics

## Tech Stack

Python · FastAPI · Uvicorn · Requests · Postman

## Run Locally

**1. Create and activate a virtual environment (macOS/Linux):**

`python3 -m venv .venv`

`source .venv/bin/activate`

**2. Install dependencies:**

`python -m pip install -r requirements.txt`

**3. Start the API:**

`python -m uvicorn main:app --reload`

**4. Open API documentation:**

`http://127.0.0.1:8000/docs`

**5. Run diagnostics (in a second terminal):**

`python api_diagnostics.py`

Demo API key: `demo-key-123`

## Incident Reports

- [INC-001 — Authentication Failure](incidents/INC-001-authentication.md)
- [INC-002 — Provider B Unavailable](incidents/INC-002-provider-unavailable.md)
- [INC-003 — Provider C Rate Limit](incidents/INC-003-rate-limit.md)

## Scope

All organizations and provider responses are simulated. The lab focuses on API troubleshooting, incident reproduction, diagnostics, and verification.