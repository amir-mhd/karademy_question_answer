from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Question 
from .forms import QuestionForm


class HomeListView(ListView):
    queryset = Question.objects.all()
    context_object_name = "questions"
    template_name = "question/question.html"
    ordering = ["-created_date"]


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question/question_detail.html'


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question/ask_question.html'
