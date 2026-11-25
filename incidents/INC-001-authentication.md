# INC-001 — API Authentication Failure

**Symptom:** Organization search returns 401 Unauthorized.

**Reproduction:** Send `GET /api/v1/organizations?domain=caspian.example` with an invalid `X-API-Key`.

**Evidence:** HTTP 401 with `{"detail":"Invalid or missing API key"}`.

**Root cause:** The API key does not match the expected demo credential.

**Resolution:** Replace the invalid key with the correct test credential.

**Verification:** Confirmed HTTP 401 and the expected error payload in Postman. Retested with a valid API key and verified HTTP 200, organization data, and `count: 1`.