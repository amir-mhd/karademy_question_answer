from django.urls import path
from .views import HomeListView, QuestionCreateView, QuestionDetailView, UpdateQuestionView


urlpatterns = [
    path('', HomeListView.as_view(), name="questions"),
    path("ask_question/", QuestionCreateView.as_view(), name="ask_question"),
    path("question_detail/<int:pk>", QuestionDetailView.as_view(), name="question_detail"),
    path("update_question/<int:pk>", UpdateQuestionView.as_view(), name="update_question"),
]