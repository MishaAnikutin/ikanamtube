from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import UserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'name', 'description', 'icon', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('icon', 'name', 'description')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('icon', 'name', 'description')}),
    )
