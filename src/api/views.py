from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from accounts.models import Customer
from api.serializers import (CustomerSerializer, QuestionSerializer,
                             QuizSerializer)
from core.permissions import IsSuperUser
from quizez.models import Question, Quiz


class UserViewSet(ModelViewSet):
    queryset = Customer.objects.filter(is_superuser=False)
    serializer_class = CustomerSerializer


class QuestionDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated | IsSuperUser]
    serializer_class = QuestionSerializer

    def get_object(self):
        return Question.objects.get(quiz__pk=self.kwargs.get("pk"), order_number=self.kwargs.get("order"))


class QuizListView(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
