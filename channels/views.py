from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import Channel
from .forms import CustomUserCreationForm, CustomUserChangeForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'channels/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'channels/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('channels:dashboard')
        else:
            error = "Неверное имя пользователя или пароль."
            return render(request, 'channels/login.html', {'error': error})
    return render(request, 'channels/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# @login_required
def dashboard_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'channels/dashboard.html', {'form': form})


def channel_list(request):
    channels = Channel.objects.all()
    return render(request, "channels/channel_list.html", {"channels": channels})
