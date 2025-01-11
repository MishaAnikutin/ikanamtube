from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Channel
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(Channel)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Channel
    list_display = ('username', 'email', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('icon', 'description')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('icon', 'description')}),
    )
