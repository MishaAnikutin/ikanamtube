from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "description", "video_file", "video_cover_file"]

    def clean_video_file(self):
        video_file = self.cleaned_data.get("video_file")
        if not video_file:
            raise forms.ValidationError("Файл видео отсутствует")

        if not video_file.name.lower().endswith(".mp4"):
            raise forms.ValidationError("Разрешены файлы только формата .mp4")

        return video_file
