from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'major', 'weight', 'is_active')
    list_filter = ('grade', 'is_active')
    search_fields = ('name', 'major', 'motto', 'message')
    list_per_page = 20