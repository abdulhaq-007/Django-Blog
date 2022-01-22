from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'post_text']
    list_filter = ['created_at', 'user']
    prepopulated_fields = {"slug":("title",)}

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_photo', 'status_info']

admin.site.register(Comment)