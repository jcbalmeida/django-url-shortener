from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_GET
from rest_framework import permissions, viewsets

from .models import Url
from .serializers import UrlSerializer


class UrlViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


@require_GET
def follow(request, slug):
    instance = get_object_or_404(Url, pk=slug)
    instance.register_click()
    return redirect(instance.full_url)
