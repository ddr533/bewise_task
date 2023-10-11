from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .serializers import QuestionSerializer
from .tasks import fetch_and_save_questions


class QuizView(APIView):
    def post(self, request):
        questions_num = request.data.get('questions_num')
        fetch_and_save_questions.delay(questions_num)
        question = Question.objects.last()
        if not question:
            return Response(data={})
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def get(self, request):
        """Необходима на получения доступа к browsable API."""
        return Response()
