from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.Charfield("Post nomi", max_length=150)
    slug = models.Slugfield("*", max_length=150)
    image = models.ImageField(upload_to='')