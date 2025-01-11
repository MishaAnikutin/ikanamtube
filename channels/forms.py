from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Channel


class CustomUserCreationForm(UserCreationForm):
    icon = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Channel
        fields = ('username', 'email', 'icon', 'description')


class CustomUserChangeForm(UserChangeForm):
    icon = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Channel
        fields = ('username', 'email', 'icon', 'description')
