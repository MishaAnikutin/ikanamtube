from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from users.models import CustomUser


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput)
    email = forms.EmailField(
        max_length=255,
        required=True,
        help_text='Обязательное поле. Введите действующий адрес электронной почты.'
    )

    icon = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ('name', 'username', 'email',  'icon', 'description', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя', 'class': 'form-control'})
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control'}),
    )


class CustomUserChangeForm(UserChangeForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput())

    class Meta:
        model = CustomUser
        fields = ('name', 'username', 'icon', 'description')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'description', 'icon']
