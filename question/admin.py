from django.contrib import admin
from .models import Question, Answer, Tag, Category

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Category)

