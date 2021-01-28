from django.contrib import admin
from .models import Profile

# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "git_url")
    search_fields = ("user", "bio", "git_url")
    raw_id_fields = ("user",)    
