from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomUserForm
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('login')
