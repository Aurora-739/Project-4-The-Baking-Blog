from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    summernote_fields = ('content',)

admin.site.register(Comment)