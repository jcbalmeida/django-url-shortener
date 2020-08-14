from celery import shared_task
from celery.utils.log import get_task_logger
from django.utils.timezone import now

from .models import Url


logger = get_task_logger(__name__)


@shared_task
def clear_expired_links():
    expired_links = Url.objects.filter(expires_at__lt=now())
    if expired_links.exists():
        logger.info("Removing {} links".format(expired_links.count()))
        expired_links.delete()
    else:
        logger.info("No links to delete by now")
