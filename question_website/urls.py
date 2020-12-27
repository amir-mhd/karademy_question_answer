from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views as question_website_views
from users import views as users_views
from question import views as question_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/", question_website_views.about ,name="about"),
    path("", include("question.urls")),
    path("register/", users_views.UserRegisterView.as_view(), name="register"),
    path("ask_question/", question_views.QuestionCreateView.as_view(), name="ask_question"),
    # path("question_detail/<int:pk>", question_views.QuestionDetailView.as_view(), name="question_detail"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
