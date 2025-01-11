from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import StreamingHttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Video
from .forms import VideoForm


class VideoUploadView(LoginRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'videos/video_upload.html'
    success_url = reverse_lazy('videos:video_list')
    login_url = reverse_lazy('channels:login')

    def form_valid(self, form):
        form.instance.channel = self.request.user
        return super().form_valid(form)


class VideoStreamView(View):
    def get(self, request, pk, *args, **kwargs):
        video = get_object_or_404(Video, pk=pk)
        file_handle = video.video_file.open('rb')
        response = StreamingHttpResponse(file_handle, content_type='video/mp4')

        response['Content-Length'] = video.video_file.size
        response['Accept-Ranges'] = 'bytes'
        return response


class VideoListView(ListView):
    model = Video
    template_name = 'videos/video_list.html'
    context_object_name = 'videos'
    paginate_by = 10

    def get_queryset(self):
        return Video.objects.order_by('-uploaded_at')


class VideoDetailView(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'
    context_object_name = 'video'


