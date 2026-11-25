import logging
from fastapi import FastAPI, Header, HTTPException, Response
from uuid import uuid4

app = FastAPI(title="Intelligence API - Support Incident Lab")
logger = logging.getLogger("uvicorn.error")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

organizations = [
    {
        "name": "Caspian Technologies",
        "domain": "caspian.example",
        "country": "Azerbaijan",
        "source": "provider_a"
    },
    {
        "name": "Vistula Analytics",
        "domain": "vistula.example",
        "country": "Poland",
        "source": "provider_b"
    }
]

provider_status = {
    "provider_a": True,
    "provider_b": False
}

@app.get("/api/v1/organizations")
def search_organizations(
    domain: str,
    response: Response,
    x_api_key: str | None = Header(default=None)
):
    if x_api_key != "demo-key-123":
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    request_id = str(uuid4())
    response.headers["X-Request-ID"] = request_id

    for org in organizations:
        if org["domain"] == domain and not provider_status.get(org["source"], False):
            logger.warning(
                "request_id=%s provider=%s status=unavailable domain=%s",
                request_id,
                org["source"],
                domain
            )

            raise HTTPException(
                status_code=503,
                detail=f"Data provider {org['source']} is temporarily unavailable",
                headers={"X-Request-ID": request_id}
            )

    results = [
        org for org in organizations
        if org["domain"] == domain
        and provider_status.get(org["source"], False)
    ]

    logger.info(
        "request_id=%s domain=%s result_count=%d",
        request_id,
        domain,
        len(results)
    )

    return {
        "results": results,
        "count": len(results)
    }

@app.get("/mock/providers/provider-c/search")
def provider_c_search(domain: str):
    request_id = str(uuid4())

    logger.warning(
        "request_id=%s provider=provider_c status=rate_limited domain=%s",
        request_id,
        domain
    )

    raise HTTPException(
        status_code=429,
        detail="Provider C rate limit exceeded",
        headers={
            "Retry-After": "5",
            "X-Request-ID": request_id
        }
    )