from django.contrib import admin

from quizez.models import Category, Choice, Question, Quiz, Result

admin.site.register([Choice, Result, Question, Category, Quiz])
