from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from .utils import base62


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

    def save(self, *args, **kwargs):
        if self._state.adding and not self.slug:
            self.slug = base62.random(5)  # TODO: parametrizar

        super().save(*args, **kwargs)
