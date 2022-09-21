from django.contrib.auth import get_user_model
from django.db import models


class Quiz(models.Model):
    category = models.ForeignKey(to="quizez.Category", related_name="quizzes", on_delete=models.CASCADE)


class Result(models.Model):
    user = models.ForeignKey(to=get_user_model(), related_name="results", on_delete=models.CASCADE)
    quiz = models.ForeignKey(to="quizez.Quiz", related_name="results", on_delete=models.CASCADE)


class Question(models.Model):
    quiz = models.ForeignKey(to="quizez.Quiz", related_name="questions", on_delete=models.CASCADE)


class Choice(models.Model):
    question = models.ForeignKey(to="quizez.Question", related_name="choices", on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=512)
