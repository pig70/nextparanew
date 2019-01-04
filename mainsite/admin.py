from django.contrib import admin
from mainsite.models import OriginalStory, UserStoryParagraphs


@admin.register(UserStoryParagraphs)
class UserStoryParagraphsAdmin(admin.ModelAdmin):
    list_display = ('short_user_paragraph', 'paragraph_author', 'user_paragraph_date',)
    ordering = ('-user_paragraph_date',)
    list_filter = ('user_paragraph_date',)
    search_fields = ('user_paragraph',)


@admin.register(OriginalStory)
class OriginalStoryAdmin(admin.ModelAdmin):
    list_display = (
        'story_headline', 'story_paragraph_author', 'short_original_paragraph', 'slug', 'story_publish_date',)
    ordering = ('-story_publish_date',)
    search_fields = ('story_headline',)
    list_filter = ('story_publish_date',)
    prepopulated_fields = {'slug': ('story_headline',)}