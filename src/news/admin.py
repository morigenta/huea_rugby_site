from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'published_at', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'content')