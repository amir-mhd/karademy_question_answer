from django.urls import path
from .views import UserRegisterView, UserProfileView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    path("password/", PasswordsChangeView.as_view(), name="change_password"),
]
