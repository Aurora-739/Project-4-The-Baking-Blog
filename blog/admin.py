from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'ingredients']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('steps', 'ingredients', 'cooking_utensils')

admin.site.register(Comment)