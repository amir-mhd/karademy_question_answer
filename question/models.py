from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse_lazy

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم برچسب", unique=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    edited_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")

    class Meta:
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب ها"
        db_table = "Tag"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="دسته بندی")
    parent = models.ForeignKey("self", verbose_name=("دسته بندی سطح بالا"), on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    edited_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندیها"
        db_table = "Category"
        ordering = ("created_date",)

    def __str__(self):
        return self.name


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="پرسنده")
    title = models.CharField(max_length=255, verbose_name="عنوان پرسش")
    description = RichTextField(verbose_name="متن پرسش")
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    slug = models.SlugField(null=True, allow_unicode=True, blank=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    edited_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    likes = models.ManyToManyField(User, related_name="question_like", blank=True)
    category = models.ForeignKey(Category, related_name="articles", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'
        ordering = ["-created_date"] 
        db_table = 'Question'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Question, self).save(*args, **kwargs)        
        if not self.slug:
            super().save(*args, **kwargs)
        self.slug = slugify(self.title)

    def get_absolute_url(self):
        return reverse_lazy('question_detail', args=[str(self.id)])

    def likes_count(self):
        return self.likes.count()


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='پاسخ دهنده')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='سوال مرتبط')
    description = RichTextField(verbose_name='متن جواب')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    edited_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")

    class Meta:
        verbose_name = "پاسخ"
        verbose_name_plural = "پاسخ ها"
        db_table = "Answers"

    def __str__(self):
        return f"{self.question.title} answer"
        