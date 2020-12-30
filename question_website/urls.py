from django.contrib import admin
from django.urls import path, include
from . import views as question_website_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/", question_website_views.AboutTemplateView.as_view() ,name="about"),
    path("", include("question.urls")),
    path("users", include("users.urls")),
]

