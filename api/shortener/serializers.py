from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["slug", "full_url", "expires_at", "created_at", "clicks"]
        read_only_fields = ["created_at", "clicks"]

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
