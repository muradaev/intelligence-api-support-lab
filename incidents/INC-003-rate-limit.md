# INC-003 — Provider C Rate Limit

**Symptom:** A data provider rejects requests with HTTP 429 Too Many Requests.

**Reproduction:** Send a GET request to `/mock/providers/provider-c/search`.

**Evidence:** HTTP 429, `Retry-After: 5`, and a matching request ID in the server log.

**Root cause:** The mock provider is configured to simulate upstream rate limiting.

**Recommended action:** Respect the retry interval, avoid aggressive repeated requests, and investigate request volume.

**Verification:** Verified HTTP 429, the expected error payload, and `Retry-After: 5` in Postman. Confirmed the expected response status and retry interval using the Python diagnostic script.

**Notes:** Endpoint simulates hard upstream rate-limiting (HTTP 429 + Retry-After header) to demonstrate rate-limit responses and Retry-After handling.