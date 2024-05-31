from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_parent = models.BooleanField(default=False)


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    age_group = models.IntegerField()  # 9-17
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
