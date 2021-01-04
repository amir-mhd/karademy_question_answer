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
    

class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question/ask_question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateQuestionView(UpdateView):
    model = Question
    fields = ['title', 'description', 'tags']
    template_name = "question/update_question.html"
 