from django.db import models
from django.utils.text import slugify

# Create your models here.
# save a shortend link - name, url, slug, # of click
class Link(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    click = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.slug}"
    
    def click(self):
        self.click += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)    