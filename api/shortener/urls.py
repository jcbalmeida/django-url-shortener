from django.urls import include, path
from rest_framework import routers
from . import views


app_name = "shortener"
router = routers.DefaultRouter()
router.register(r"urls", views.UrlViewSet)

urlpatterns = [
    path(r"api/", include(router.urls)),
    path(r"<slug:slug>", views.follow, name="follow"),
]
