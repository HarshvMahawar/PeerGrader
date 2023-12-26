# peer_grading_app/models.py

from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title



class Rubric(models.Model):
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    question_number = models.PositiveIntegerField()
    max_marks = models.PositiveIntegerField()

    def __str__(self):
        return f"Question {self.question_number}"


