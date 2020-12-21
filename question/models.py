from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم برچسب")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    edited_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")

    class Meta:
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب ها"
        db_table = "Tag"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="دسته بندی", blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    edited_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندیها"
        db_table = "Category"

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="پرسنده")
    title = models.CharField(max_length=255, verbose_name="عنوان پرسش")
    description = RichTextField(verbose_name="متن پرسش")
    tag = models.ForeignKey(Tag, blank=True)
    slug = models.SlugField(null=True, allow_unicode=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    edited_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    
    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'
        ordering = ('-date_created',) 
        db_table = 'Question'

    def __str__(self):s
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='پاسخ دهنده')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='سوال مرتبط', related_name='question_answers')
    description = RichTextField(verbose_name='متن جواب')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_edited = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش') 

    class Meta:
        verbose_name = "پاسخ"
        verbose_name_plural = "پاسخ ها"
        db_table = "Answers"

    def __str__(self):
        return f"{self.question.title} answer"
        