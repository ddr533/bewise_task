from django.urls import path

from .views import QuizView

app_name = 'quize'


urlpatterns = [
    path('', QuizView.as_view(), name='question-create'),
]
