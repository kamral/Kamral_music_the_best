from django.shortcuts import render

# Create your views here.
from .models import CustomUser
from django.views.generic import CreateView
from .forms import CustomUserCreationChangeForm,CustomUserCreationFrom
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class SignUpView(CreateView):
    form_class = CustomUserCreationFrom
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

