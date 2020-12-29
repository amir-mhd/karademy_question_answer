from django.shortcuts import render
from django.views.generic import TemplateView

class AboutTemplateView(TemplateView):
    template_name = "question_website/about.html"
