from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Question 
from .forms import QuestionForm


class HomeListView(ListView):
    queryset = Question.objects.all()
    context_object_name = "questions"
    template_name = "question/question.html"


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question/question_detail.html'
    

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question/ask_question.html'
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateQuestionView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['title', 'description', 'tags']
    # create and update view can use the same template
    template_name = "question/ask_question.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False
