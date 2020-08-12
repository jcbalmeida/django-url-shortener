from django.db import models
from django.utils.timezone import now
from datetime import timedelta


def expires_at_default():
    return now() + timedelta(days=7)  # TODO: parametrizar


class Url(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    full_url = models.URLField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(
        db_index=True, default=expires_at_default
    )
    clicks = models.PositiveIntegerField(default=0)
