from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import ListView

from videos.models import Video
from .forms import SignUpForm, UserLoginForm, CustomUserChangeForm, UserProfileForm
from .models import CustomUser


class SignupView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "users/signup.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)
        print("FILES:", request.FILES)

        if form.is_valid():
            form.save()
            return redirect("users:login")

        return render(request, "users/signup.html", {"form": form})


def signup(request):
    print(1)
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password1"),
            )
            login(request, user)
            return redirect("home")
        else:
            return render(
                request, "users/signup.html", {"form": form, "err": form.errors}
            )

    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def personal_account_view(request):
    videos = Video.objects.filter(channel=request.user)

    return render(
        request,
        "users/personal_account.html",
        {
            "videos": videos,
        },
    )


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserProfileForm(instance=request.user)
        return render(request, "users/profile.html", {"form": form})

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("users:profile")

        return render(request, "users/profile.html", {"form": form})


class ChannelView(View):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        videos = Video.objects.filter(channel=user)

        return render(
            request,
            "users/channel.html",
            {
                "user": user,
                "videos": videos,
            },
        )


class UserListView(ListView):
    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users"
    paginate_by = 10

    def get_queryset(self):
        return CustomUser.objects.all()
