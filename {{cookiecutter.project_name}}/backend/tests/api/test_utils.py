"""Tests for the `utils` router."""
from fastapi.testclient import TestClient

from app.core.config import settings


def test_ping(client: TestClient) -> None:
    """
    When a request is made to `/ping`
    Then a `"pong"` is returned
    """
    resp = client.get(f"{settings.api_path}/ping")

    data = resp.json()

    assert data == "pong"
