from django.contrib import admin
from .models import Category, FAQ

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order', 'name')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'is_published', 'order')
    list_filter = ('category', 'is_published')
    search_fields = ('question', 'answer')
    ordering = ('category', 'order', 'created_at')