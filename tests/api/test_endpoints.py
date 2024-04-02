from fastapi import status
from fastapi.testclient import TestClient
from pydantic import HttpUrl
from sqlalchemy.orm import Session

import models
from core.config import settings


def test_create_url(client: TestClient, db: Session):
    original_url = "https://url.com"
    payload = {"original_url": original_url}
    response = client.post(f"{settings.api_v1_route}/urls", json=payload)

    assert response.status_code == status.HTTP_201_CREATED

    content = response.json()

    assert content["original_url"] == str(HttpUrl(original_url))
    assert "short_url" in content


def test_create_url_is_idempotent(client: TestClient, db: Session):
    original_url = "https://url.com"
    payload = {"original_url": original_url}
    response_one = client.post(f"{settings.api_v1_route}/urls", json=payload)
    response_two = client.post(f"{settings.api_v1_route}/urls", json=payload)

    assert response_one.status_code == status.HTTP_201_CREATED
    assert response_two.status_code == response_one.status_code

    content_one = response_one.json()
    content_two = response_two.json()

    assert content_one == content_two


def test_redirect_original_url_returns_404_on_non_existent_url(
    client: TestClient, db: Session
):
    response = client.get(f"{settings.api_v1_route}/nourl")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_redirect_original_url_returns_original_url(
    client: TestClient, db: Session, url_sample: models.URL
):
    response = client.get(
        f"{settings.api_v1_route}/{url_sample.short_url}", follow_redirects=False
    )

    assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT
    assert response.is_redirect

    headers = response.headers

    assert headers["location"] == url_sample.original_url


def test_redirect_original_url_returns_400_on_invalid_url(
    client: TestClient, db: Session
):
    response = client.get(f"{settings.api_v1_route}/invalid*")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
