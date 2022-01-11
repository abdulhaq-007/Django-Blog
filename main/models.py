from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    name = models.CharField("Name", max_length=100)
    surname = models.CharField("Surname", max_length=100)
    age = models.CharField("Age", max_length=50)
    year = models.CharField("Year", max_length=30)
    image = models.ImageField("Image", upload_to='images/')

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField("Post nomi", max_length=150)
    slug = models.SlugField("*", max_length=150)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])