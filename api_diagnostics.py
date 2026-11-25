import requests

BASE_URL = "http://127.0.0.1:8000"

checks = [
    ("Valid organization", "/api/v1/organizations",
     "caspian.example", "demo-key-123", 200),

    ("Invalid API key", "/api/v1/organizations",
     "caspian.example", "wrong-key-999", 401),

    ("Provider B unavailable", "/api/v1/organizations",
     "vistula.example", "demo-key-123", 503),

    ("Provider C rate limit", "/mock/providers/provider-c/search",
     "caspian.example", "demo-key-123", 429)
]

for name, path, domain, api_key, expected_status in checks:
    try:
        response = requests.get(
            BASE_URL + path,
            params={"domain": domain},
            headers={"X-API-Key": api_key},
            timeout=5
        )

        result = "PASS" if response.status_code == expected_status else "FAIL"

        print(f"{result} | {name}")
        print(f"  HTTP: {response.status_code} | Expected: {expected_status}")
        print(f"  Request ID: {response.headers.get('X-Request-ID', 'N/A')}")

        if response.status_code == 429:
            print(f"  Retry-After: {response.headers.get('Retry-After')} seconds")

    except requests.exceptions.RequestException as error:
        print(f"ERROR | {name}: {error}")

    print("-" * 45)