# app.py
import os
import requests

# Load secret from environment; fail fast if missing.
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY environment variable is not set. Configure a secret manager or set the env var.")


def fetch_user_data(user_id, timeout=10):
    """Fetches data from an external API with basic hardening.

    - Uses `API_KEY` from environment (never hard-coded).
    - Sets a request timeout to avoid hanging.
    - Raises on non-2xx status codes.
    - Validates JSON decoding.
    """
    url = f"https://api.example.com/data/{user_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Failed to fetch user data: {exc}") from exc

    try:
        return response.json()
    except ValueError as exc:
        raise RuntimeError("Response did not contain valid JSON") from exc


if __name__ == "__main__":
    print("Starting application...")
    # Do not log or print secrets. Ensure API_KEY is provided via environment.
    data = fetch_user_data(5)
    print("Data fetched successfully.")