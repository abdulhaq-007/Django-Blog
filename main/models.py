from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.FileField(upload_to='profile_photos')
    status_info = models.CharField(default="Your status put here", max_length=1000)

    def str(self):
        return f'{self.user.username} Profile'

class Tag(models.Model):
    name = models.CharField("Tag nomi",max_length=100)
    slug = models.SlugField("*", max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"   

class Category(models.Model):
    name = models.CharField("Kategoriya nomi", max_length=100,)
    slug = models.SlugField("*", max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("blog:category_detail", kwargs={"category_slug":self.slug})

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.name = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name=("Tags"))
    title = models.CharField(max_length=200)
    slug = models.SlugField("*", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    post_text = models.CharField(max_length=2000)
    post_picture = models.ImageField(upload_to='post_picture')

    def str(self):
        return self.user.username

    class Meta:
        ordering = ['-id']


class Video_post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post_text = models.CharField(max_length=2000)
    post_picture = models.FileField(upload_to='post_picture')

# Model for storing comment
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_text = models.CharField(default="", max_length=2000)


class Reply_comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_text = models.CharField(default="", max_length=2000)