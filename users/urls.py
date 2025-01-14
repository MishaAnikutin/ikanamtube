from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    # Авторизация
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    # Другие каналы
    path("", views.UserListView.as_view(), name="user_list"),
    path("channel/<str:username>/", views.ChannelView.as_view(), name="channel"),
    # Твой канал
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("personal_account/", views.personal_account_view, name="personal_account"),
]
