import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Url as url_model


@pytest.fixture
def auto_login_user(django_user_model):
    def make_auto_login(client=None, user=None):
        if client is None:
            client = APIClient()
        if user is None:
            user = django_user_model.objects.create_user(
                username="user1", password="foobar"
            )
        client.force_authenticate(user=user)
        return client, user

    return make_auto_login


@pytest.mark.django_db
def test_shorten_url(auto_login_user):
    client, user = auto_login_user()
    url = reverse("shortener:url-list")

    data = {
        "full_url": "https://www.github.com",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == 201

    json_response = response.json()
    assert "short_url" in json_response

    slug = json_response["slug"]
    assert url_model.objects.filter(pk=slug).exists()
    assert url_model.objects.get(pk=slug).full_url == data["full_url"]


@pytest.mark.django_db
def test_shorten_url_passing_slug(auto_login_user):
    client, user = auto_login_user()
    url = reverse("shortener:url-list")

    data = {
        "slug": "user-defined",
        "full_url": "https://www.github.com",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == 201
    json_response = response.json()
    assert "short_url" in json_response
    assert json_response["slug"] == "user-defined"


@pytest.mark.django_db
def test_shorten_url_with_existing_slug(auto_login_user):
    client, user = auto_login_user()
    url = reverse("shortener:url-list")

    data = {
        "slug": "user-defined",
        "full_url": "https://www.github.com",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == 201
    assert "short_url" in response.json()

    second_response = client.post(url, data, format="json")
    assert second_response.status_code == 400
    print(second_response.json())
    assert url_model.objects.filter(pk="user-defined").count() == 1


@pytest.mark.django_db
def test_follow_short_url():
    url_instance = url_model.objects.create(full_url="https://www.github.com")
    client = APIClient()
    url = reverse("shortener:follow", args=(url_instance.slug,))
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == url_instance.full_url
