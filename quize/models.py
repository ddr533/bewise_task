from django.db import models


class Question(models.Model):
    question_id = models.IntegerField(unique=True, db_index=True)
    question_text = models.CharField(max_length=1250)
    answer_text = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.question_text
