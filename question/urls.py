from django.urls import path
from .views import ( HomeListView,
    QuestionCreateView,
    QuestionDetailView,
    QuestionUpdateView,
    QuestionDeletView,
    LikeView,
    CategoryListView, 
    CategoryArticlesList)


urlpatterns = [
    path('', HomeListView.as_view(), name="questions"),
    path("ask_question/", QuestionCreateView.as_view(), name="ask_question"),
    path("question_detail/<int:pk>/", QuestionDetailView.as_view(), name="question_detail"),
    path("question_detail/<int:pk>/update/", QuestionUpdateView.as_view(), name="update_question"),
    path("question_detail/<int:pk>/delete/", QuestionDeletView.as_view(), name="delete_question"),
    path("question_detail/<int:pk>/like/", LikeView, name="question_like"),
    path("category_list/", CategoryListView.as_view(), name="category_list"),
    path("category_articles_list/<int:category_id>/<str:category_slug>", CategoryArticlesList.as_view(), name="category_articles_list"),
]