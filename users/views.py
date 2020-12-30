from .forms import UserRegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("questions") # should become login page when it created