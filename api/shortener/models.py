from django.db import models, IntegrityError
from django.utils.timezone import now
from datetime import timedelta
from .utils import base62
from django.conf import settings


def expires_at_default():
    return now() + timedelta(seconds=settings.SHORTENER_DEFAULT_DURATION)


def get_random_slug(tries):
    return base62.random(settings.SHORTENER_DEFAULT_LENGTH + tries)


class Url(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    full_url = models.URLField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(
        db_index=True, default=expires_at_default
    )
    clicks = models.PositiveIntegerField(default=0)

    def register_click(self):
        self.clicks = models.F("clicks") + 1
        self.save()

    def get_short_url(self):
        return "{}/{}".format(settings.BASE_URL, self.slug)

    def save(self, *args, **kwargs):
        if (
            self._state.adding and not self.slug
        ):  # slug defaults to random string
            for i in range(3):
                self.slug = get_random_slug(i)
                try:
                    super().save(*args, **kwargs)
                    return
                except IntegrityError:
                    continue
            raise KeyError("Could not generate unique slug")
        else:
            super().save(*args, **kwargs)
