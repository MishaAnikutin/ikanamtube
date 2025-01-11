from django.db import models
from django_s3_storage.storage import S3Storage
from django.contrib.auth.models import AbstractUser

from ikanamtube.settings import AWS_STORAGE_BUCKET_NAME


storage = S3Storage(aws_s3_bucket_name=AWS_STORAGE_BUCKET_NAME)


def icons_upload_to(instance, filename):
    return f"channel_icons/{instance.username}/{filename}"


class Channel(AbstractUser):
    description = models.TextField(blank=True)
    icon = models.ImageField(storage=storage, upload_to=icons_upload_to)
