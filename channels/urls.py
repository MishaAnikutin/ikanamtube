from django.urls import path

from . import views

app_name = 'channels'

urlpatterns = [
    path("", views.channel_list, name="channel_list"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
