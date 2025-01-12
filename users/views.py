from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.views import View

from .forms import SignUpForm, UserLoginForm, CustomUserChangeForm, UserProfileForm
from .models import CustomUser


class SignupView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)
        print('FILES:', request.FILES)

        if form.is_valid():
            form.save()
            return redirect('users:login')

        return render(request, 'users/signup.html', {'form': form})


def signup(request):
    print(1)
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/signup.html', {'form': form, 'err': form.errors})

    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


def logout_view(request):
    logout(request)
    return redirect('home')


def list_users(request):
    users = CustomUser.objects.all()
    return render(request, "users/users_list.html", {"users": users})


@login_required
def personal_account_view(request):
    return render(request, 'users/personal_account.html', {'form': CustomUserChangeForm()})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserProfileForm(instance=request.user)
        return render(request, 'users/profile.html', {'form': form})

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')

        return render(request, 'users/profile.html', {'form': form})
