from .forms import UserRegisterForm, UserEditForm
from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    # success_message = f"{username} was created successfully"
    # success_message = f"{User.get_username(self)} was created successfully"
    # def success_message(self):
    #     username = get_username(self.User)
    #     return f"{username} was created successfully"
    # def get_success_message(self, cleaned_data):
    #     return self.f"{username} was created sucessfully" % dict(cleaned_data, username=self.object.username,)


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