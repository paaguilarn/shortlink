from fastapi import status
from fastapi.testclient import TestClient
from pydantic import HttpUrl
from sqlalchemy.orm import Session

from core.config import settings


def test_create_url(client: TestClient, db: Session):
    original_url = "https://url.com"
    payload = {
        "original_url": original_url
    }
    response = client.post(f"{settings.api_v1_route}/urls", json=payload)

    assert response.status_code == status.HTTP_201_CREATED

    content = response.json()

    assert content["original_url"] == str(HttpUrl(original_url))
    assert "short_url" in content


def test_create_url_is_idempotent(client: TestClient, db: Session):
    original_url = "https://url.com"
    payload = {
        "original_url": original_url
    }
    response_one = client.post(f"{settings.api_v1_route}/urls", json=payload)
    response_two = client.post(f"{settings.api_v1_route}/urls", json=payload)

    assert response_one.status_code == status.HTTP_201_CREATED
    assert response_two.status_code == response_one.status_code

    content_one = response_one.json()
    content_two = response_two.json()

    assert content_one == content_two
