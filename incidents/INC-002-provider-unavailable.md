# INC-002 — Provider B Data Unavailable

**Symptom:** A known organization disappears from search results despite HTTP 200.

**Reproduction:** Set `provider_b = False` and request `vistula.example`.

**Evidence:** The API initially returned `results: []` and `count: 0`. Server logs identified `provider_b` as unavailable using the request ID.

**Root cause:** The simulated provider outage was incorrectly treated as an empty search result.

**Resolution:** Updated the endpoint to return HTTP 503 instead of misleading HTTP 200.

**Verification:** Verified HTTP 503, the expected error payload, and `X-Request-ID` propagation in Postman. Correlated the request ID with the provider warning in server logs.