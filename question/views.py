from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Question 
from .forms import QuestionForm

class HomeListView(ListView):
    model = Question
    template_name = "question/questions.html"
    

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question/question_detail.html'


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question/ask_question.html'
