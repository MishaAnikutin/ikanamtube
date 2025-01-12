from django.urls import path
from .views import (
    VideoUploadView,
    VideoStreamView,
    VideoListView,
    VideoDetailView,
    LikeDislikeView
)

app_name = 'videos'

urlpatterns = [
    path('', VideoListView.as_view(), name='video_list'),

    path('upload/', VideoUploadView.as_view(), name='video_upload'),
    path('<int:pk>/stream/', VideoStreamView.as_view(), name='video_stream'),
    path('<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
    path('<int:video_id>/like/', LikeDislikeView.as_view(), name='like_dislike'),
]
