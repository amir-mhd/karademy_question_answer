from .forms import UserRegisterForm, UserEditForm
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    success_message = "account was created successfully"


class UserEditView(SuccessMessageMixin, UpdateView):
    form_class = UserEditForm     
    template_name = "users/edit_profile.html"
    success_url = reverse_lazy("questions")
    success_message = "profile edited successfully" 

    # show the default information in the form fields
    def get_object(self):
        return self.request.user


class UserProfileView(TemplateView):
    template_name = "users/profile.html"
    success_url = "profile"
    

class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("login")
    template_name = "users/change_password.html"
    success_message = "password changed successfully"