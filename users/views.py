from .forms import UserRegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User



class UserRegisterView(SuccessMessageMixin, CreateView):
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