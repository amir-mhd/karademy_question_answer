from django.contrib import admin
from .models import Question, Answer, Category

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "slug", "category", "created_date", "edited_date")
    list_filter = ("author", "category")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description")
    #change the author field, make it easier to look up betwen users
    raw_id_fields = ("author",)
    ordering = ("created_date", "edited_date")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("author", "question", "created_date", "edited_date")
    raw_id_fields = (("author",))
    search_fields = ("title", "description")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "created_date", "edited_date")
    list_filter = ("parent",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "parent")


