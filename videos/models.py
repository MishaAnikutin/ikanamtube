from django.db import models
from django_s3_storage.storage import S3Storage

from users.models import CustomUser
from ikanamtube.settings import AWS_STORAGE_BUCKET_NAME

storage = S3Storage(aws_s3_bucket_name=AWS_STORAGE_BUCKET_NAME)


def videos_upload_to(instance, filename):
    return f"videos/{instance.channel.username}/{filename}"


def video_cover_upload_to(instance, filename):
    return f"videos/{instance.channel.username}/{filename}"


class Video(models.Model):
    channel = models.ForeignKey(
        CustomUser, related_name="videos", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video_file = models.FileField(storage=storage, upload_to=videos_upload_to)
    video_cover_file = models.ImageField(
        storage=storage, upload_to=video_cover_upload_to, blank=True, null=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LikeDislike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)

    class Meta:
        unique_together = (("user", "video"),)
