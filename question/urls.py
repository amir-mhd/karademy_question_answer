from django.urls import path
from .views import HomeListView, QuestionCreateView, QuestionDetailView, QuestionUpdateView, QuestionDeletView


urlpatterns = [
    path('', HomeListView.as_view(), name="questions"),
    path("ask_question/", QuestionCreateView.as_view(), name="ask_question"),
    path("question_detail/<int:pk>", QuestionDetailView.as_view(), name="question_detail"),
    path("update_question/<int:pk>", QuestionUpdateView.as_view(), name="update_question"),
    path("update_question/<int:pk>", QuestionDeletView.as_view(), name="delete_question"),

]