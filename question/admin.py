from django.contrib import admin
from .models import Question, Answer, Tag, Category

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "slug", "category", "created_date", "edited_date")
    list_filter = ("author", "category")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description")
    # raw_id_fields = ("author",)
    ordering = ("created_date", "edited_date")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("author", "question", "created_date", "edited_date")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "created_date", "edited_date")
    list_filter = ("parent",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "parent")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_date", "edited_date")
    ordering = ("created_date",)


