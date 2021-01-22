from .forms import UserRegisterForm, UserEditForm
from django.views.generic import CreateView, TemplateView, UpdateView
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


class UserEditView(UpdateView):
    form_class = UserEditForm 
    template_name = "users/edit_profile.html"
    success_url = reverse_lazy("profile")

    # show the default information in the form fields
    def get_object(self):
        return self.request.user


class UserProfileView(TemplateView):
    template_name = "users/profile.html"
    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("login")
    template_name = "users/change_password.html"