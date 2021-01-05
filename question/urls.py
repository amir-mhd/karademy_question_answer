from django.urls import path
from .views import HomeListView, QuestionCreateView, QuestionDetailView, QuestionUpdateView, QuestionDeletView


urlpatterns = [
    path('', HomeListView.as_view(), name="questions"),
    path("ask_question/", QuestionCreateView.as_view(), name="ask_question"),
    path("question_detail/<int:pk>", QuestionDetailView.as_view(), name="question_detail"),
    path("question_detail/<int:pk>/update", QuestionUpdateView.as_view(), name="update_question"),
    path("question_detail/<int:pk>/delete", QuestionDeletView.as_view(), name="delete_question"),

]