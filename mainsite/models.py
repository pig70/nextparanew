from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatewords
from django.utils import timezone

from userprofile.models import AuthorProfile
from tagging.models import StoryTags

#Model for the original story
class OriginalStory(models.Model):
    story_headline = models.CharField(max_length=70, blank=True)
    story_publish_date = models.DateTimeField(auto_now_add=True)
    story_first_paragraph = models.TextField(max_length=600, blank=True)
    story_paragraph_author = models.ForeignKey(
        AuthorProfile, on_delete=models.CASCADE, blank=True, null=True, related_name="author")
    slug = models.SlugField(max_length=250, null=True)
    story_tags = models.ManyToManyField(StoryTags, blank=True, null=True, related_name='tags_for_story')

    class Meta:
        verbose_name_plural ='Original stories'

    def __str__(self):
        return self.story_headline

    @property
    def short_original_paragraph(self):
        return truncatewords(self.story_first_paragraph, 20)


#Model for the paragraphs added by logged in authors
class UserStoryParagraphs(models.Model):
    user_paragraph = models.TextField(max_length=800)
    user_paragraph_date = models.DateTimeField(
        default=timezone.now, blank=True, verbose_name="Date added")
    paragraph_author = models.ForeignKey(
        AuthorProfile, on_delete=models.CASCADE, null=True, blank=True, related_name="para_author")
    story_belongs_to = models.ForeignKey(
        OriginalStory, on_delete=models.CASCADE, blank=True, null=True, related_name="paragraphs")

    class Meta:
        verbose_name_plural = 'User paragraphs'

    def __str__(self):
        return self.user_paragraph

#property within UserStoryParagraphs which defines a truncation of the paragraph for use within the admin list_display
    @property
    def short_user_paragraph(self):
        return truncatewords(self.user_paragraph, 20)