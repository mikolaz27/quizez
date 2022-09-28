"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.views import QuestionDetailView, QuizListView, UserViewSet
from quizez.models import Question

app_name = "api"
routes = routers.DefaultRouter()
routes.register("customers", UserViewSet)

urlpatterns = [
    path("", include(routes.urls)),
    path("auth/", include("rest_framework.urls")),
    path("quiz/<int:pk>/question/<int:order>/", QuestionDetailView.as_view(), name="question_detail"),
    path("quiz/", QuizListView.as_view(), name="quiz_list"),
]
