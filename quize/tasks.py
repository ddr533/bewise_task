import requests
from celery import shared_task
from django.core.cache import cache
from django.db import transaction

from .models import Question


@shared_task
def fetch_and_save_questions(num_questions):
    """Делает запросы к api для получения переданного числа (num_questions)
     уникальных вопросов и сохраняет их в БД."""

    expected_new_question = num_questions
    questions = []

    while expected_new_question:
        url = f'https://jservice.io/api/random?count={expected_new_question}'
        response = requests.get(url)
        data = response.json()
        for question_data in data:
            question_id = question_data['id']

            if cache.get(question_id) is not None:
                continue

            question_text = question_data['question']
            answer_text = question_data['answer']
            created_at = question_data['created_at']

            if not Question.objects.filter(question_id=question_id).exists():
                question = Question(
                    question_id=question_id,
                    question_text=question_text,
                    answer_text=answer_text,
                    created_at=created_at
                )
                questions.append(question)
                expected_new_question -= 1

                cache.set(question_id, True, timeout=60)

    with transaction.atomic():
        Question.objects.bulk_create(questions, batch_size=100)

    return True
