from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    create_datetime = models.DateTimeField(null=True, auto_now_add=True)
    last_update = models.DateTimeField(null=True, auto_now=True)


class Quiz(BaseModel):
    QUESTION_MAX_LIMIT = 20
    QUESTION_MIN_LIMIT = 3

    class LEVEL_CHOICES(models.IntegerChoices):
        BASIC = 0, "Basic"
        MIDDLE = 1, "Middle"
        ADVANCED = 2, "Advanced"

    category = models.ForeignKey(to="quizez.Category", related_name="quizzes", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024, blank=True, null=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.BASIC)

    image = models.ImageField(default="default.png", upload_to="media/covers")

    def questions_count(self):
        return self.questions.count()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Result(BaseModel):
    user = models.ForeignKey(to=get_user_model(), related_name="results", on_delete=models.CASCADE)
    quiz = models.ForeignKey(to="quizez.Quiz", related_name="results", on_delete=models.CASCADE)


class Question(BaseModel):
    quiz = models.ForeignKey(to="quizez.Quiz", related_name="questions", on_delete=models.CASCADE)
    order_number = models.PositiveSmallIntegerField(validators=[MaxValueValidator(Quiz.QUESTION_MAX_LIMIT)])
    text = models.CharField(max_length=512)


class Choice(BaseModel):
    question = models.ForeignKey(to="quizez.Question", related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=128)
    is_correct = models.BooleanField(default=False)


class Category(BaseModel):
    name = models.CharField(max_length=512)
