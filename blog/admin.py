from django.contrib import admin
from .models import Blog, Section, Category


class SectionInline(admin.StackedInline):
    model = Section
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    inlines = [SectionInline]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
