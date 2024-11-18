from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    difficulty = models.PositiveSmallIntegerField(default=3)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='challenges_authored')
    creation_date = models.DateTimeField("date posted", auto_now_add=True)
    likers = models.ManyToManyField(User, related_name='challenges_liked')
    answer_image = models.ImageField()
    answer_text = models.TextField()
    isweekly = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    likers =  models.ManyToManyField(User, related_name='comments_liked')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    creation_date = models.DateTimeField("date posted", auto_now_add=True)




