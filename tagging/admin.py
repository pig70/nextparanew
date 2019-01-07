from django.contrib import admin
from .models import StoryTags


@admin.register(StoryTags)
class StoryTags(admin.ModelAdmin):
    ordering = ('tags',)