from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post-image', default='post-image/no-image.png', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(blank=True, null=True)
    visibility = models.BooleanField(default=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-published',)

    def get_absolute_url(self):
        return reverse('post:post-detail', args=[str(self.id)])


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
