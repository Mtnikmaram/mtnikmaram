from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_on = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, null=True)
          
    def __str__(self):
        return self.title
    