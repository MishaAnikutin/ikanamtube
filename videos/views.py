from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import StreamingHttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Video, LikeDislike
from .forms import VideoForm


class VideoUploadView(LoginRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    template_name = "videos/video_upload.html"
    success_url = reverse_lazy("videos:video_list")
    login_url = reverse_lazy("channels:login")

    def form_valid(self, form):
        form.instance.channel = self.request.user
        return super().form_valid(form)


class VideoStreamView(View):
    def get(self, request, pk, *args, **kwargs):
        video = get_object_or_404(Video, pk=pk)
        file_handle = video.video_file.open("rb")
        response = StreamingHttpResponse(file_handle, content_type="video/mp4")

        response["Content-Length"] = video.video_file.size
        response["Accept-Ranges"] = "bytes"
        return response


class VideoListView(ListView):
    model = Video
    template_name = "videos/video_list.html"
    context_object_name = "videos"
    paginate_by = 10

    def get_queryset(self):
        return Video.objects.order_by("-uploaded_at")


class VideoDetailView(View):
    def get(self, request, pk):
        video = get_object_or_404(Video, pk=pk)

        # Получаем количество лайков и дизлайков
        likes_count = LikeDislike.objects.filter(video=video, is_like=True).count()
        dislikes_count = LikeDislike.objects.filter(video=video, is_like=False).count()

        return render(
            request,
            "videos/video_detail.html",
            {
                "video": video,
                "likes_count": likes_count,
                "dislikes_count": dislikes_count,
            },
        )


class LikeDislikeView(View):
    def post(self, request, video_id):
        video = get_object_or_404(Video, id=video_id)

        if not request.user.is_authenticated:
            return redirect(request.META.get("HTTP_REFERER"), context={'errors': 'Пользователь не авторизован'})

        like_dislike, _ = LikeDislike.objects.get_or_create(
            user=request.user, video=video
        )

        like_dislike.delete()
        like_dislike.is_like = request.POST.get("action") == "like"
        like_dislike.save()

        return redirect(request.META.get("HTTP_REFERER"))
