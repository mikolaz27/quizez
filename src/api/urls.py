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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import QuestionDetailView, QuizListView, UserViewSet
from quizez.models import Question

app_name = "api"
routes = routers.DefaultRouter()
routes.register("customers", UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Quizez API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns = [
    path("", include(routes.urls)),
    path("auth/", include("rest_framework.urls")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    path("auth/", include("djoser.urls.jwt")),
    path("quiz/<int:pk>/question/<int:order>/", QuestionDetailView.as_view(), name="question_detail"),
    path("quiz/", QuizListView.as_view(), name="quiz_list"),
]
