from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.title
