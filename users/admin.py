from django.contrib import admin
from .forms import  \
    CustomUserCreationFrom, \
    CustomUserCreationChangeForm
# Register your models here.
from.models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationFrom
    form = CustomUserCreationChangeForm
    model=CustomUser


admin.site.register(CustomUser, CustomUserAdmin)

