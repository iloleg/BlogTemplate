from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_subtitle', 'post_body', 'post_created_on')

admin.site.register(Post, PostAdmin)