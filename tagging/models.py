from django.db import models

# Tags
class StoryTags(models.Model):
    tags = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Story tags'

    def __str__(self):
        return self.tags
