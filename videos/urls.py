from django.urls import path
from .views import VideoUploadView, VideoStreamView, VideoListView, VideoDetailView

app_name = 'videos'

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video_upload'),
    path('<int:pk>/stream/', VideoStreamView.as_view(), name='video_stream'),
    path('', VideoListView.as_view(), name='video_list'),
    path('<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
]