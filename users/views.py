# users/views.py
from re import template
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

