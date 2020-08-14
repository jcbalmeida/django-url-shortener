from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
    path(r"auth/obtain_token/", obtain_jwt_token),
    path(r"auth/refresh_token/", refresh_jwt_token),
    path("", include("shortener.urls", namespace="shortener")),
]
