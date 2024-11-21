from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    post_text = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    likers = models.ManyToManyField(User, related_name='likers')
    post_date = models.DateTimeField("date posted", auto_now_add=True)

    def __str__(self):
        return f'{self.post_text} ({self.id})'

class Hashtag(models.Model):
    hashtag_text = models.CharField(max_length=140)
    tweets = models.ManyToManyField(Tweet)

    def __str__(self):
        return f'{self.hashtag_text}'



    