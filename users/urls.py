from django.urls import path
from .views import UserRegisterView, UserCreationForm


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
]
