from django.urls import path

from quizez.views import bitcoin, normalize_email

app_name = "quiz"
urlpatterns = [
    path("bitcoin/", bitcoin, name='bitcoin'),
    path("normalize_email/", normalize_email, name='normalize_email'),
]
