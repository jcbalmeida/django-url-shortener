from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.ModelSerializer):

    short_url = serializers.URLField(source="get_short_url", read_only=True)

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get("request", None)
        if request:
            method = getattr(request, "method", None)
            if method == "POST":
                fields["slug"].allow_blank = True
            elif method == "PUT":
                fields["slug"].read_only = True
        return fields

    class Meta:
        model = Url
        fields = [
            "slug",
            "short_url",
            "full_url",
            "expires_at",
            "created_at",
            "clicks",
        ]
        read_only_fields = ["short_url", "created_at", "clicks"]
