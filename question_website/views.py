from django.shortcuts import render


def about(request):
    return render(request, "question_website/about.html")
