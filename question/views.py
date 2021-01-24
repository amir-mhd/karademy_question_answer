from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from .models import Question, Category 
from .forms import QuestionForm
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin


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
    
    #check if question is liked or not, passing it to the template
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        question = get_object_or_404(Question, id=self.kwargs["pk"])
        categories = Category.objects.all()
        liked = False
        if question.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["liked"] = liked  
        context["categories"] = categories
        return context


class QuestionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question/ask_question.html'
    login_url = '/users/login/'
    success_message = "created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Question
    fields = ['title', 'description', 'tags']
    # create and update view can use the same template
    template_name = "question/ask_question.html"
    success_message = "updated successfully"

    #check if request user is the author or not
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #necessery for UserPassesTestMixin to check for permession
    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


class QuestionDeletView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Question
    template_name = "question/question_confirm_delete.html"
    success_url = "/"
    success_message = "deleted successfully"

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


class CategoryListView(ListView):
    model = Category
    template_name = "question/category_list.html"
    context_object_name = "categories"


class CategoryArticlesList(ListView):
    template_name = "question/category_article_list.html"
    context_object_name = "category_list"

    # using (get_quesryset) instead of using (model) to customize the query
    def get_queryset(self):
        """
        customize the queryset by using the (category) passed with the url
        """
        content = {
            "category": self.kwargs['category'],
            "questions": Question.objects.filter(category__id=self.kwargs["id"]),
        }
        return content
        
