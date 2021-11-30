from django.db import models
from django.urls import reverse

class Place(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_urls(self):
        return reverse("places:detail", kwargs={"slug": self.slug})

