from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "users/register.html"