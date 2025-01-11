from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'channel', 'uploaded_at')
    search_fields = ('title', 'channel__name')
    list_filter = ('channel', 'uploaded_at')
