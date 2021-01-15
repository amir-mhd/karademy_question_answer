from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Question 
from .forms import QuestionForm
from django.http import HttpResponseRedirect


def LikeView(request, pk):
    question = get_object_or_404(Question, id=request.POST.get("question_id"))
    liked = False
    if question.likes.filter(id=request.user.id).exists():
        question.likes.remove(request.user)
    else:
        question.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("question_detail", args=[str(pk)]))


class HomeListView(ListView):
    queryset = Question.objects.all()
    context_object_name = "questions"
    template_name = "question/question.html"


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question/question_detail.html'
    context_object_name = "question"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        question = get_object_or_404(Question, id=self.kwargs["pk"])

        liked = False
        if question.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["liked"] = liked  
        return context


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question/ask_question.html'
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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


class QuestionDeletView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    template_name = "question/question_confirm_delete.html"
    success_url = "/"

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False

