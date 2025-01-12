from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("", views.list_users, name="users_list"),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('personal_account/', views.personal_account_view, name='personal_account')
]
