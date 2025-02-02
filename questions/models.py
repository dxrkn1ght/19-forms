from django.db import models


class Question(models.Model):
    test = models.ForeignKey('tests.Test', on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=150)
    answer_1 = models.CharField(max_length=150)
    answer_2 = models.CharField(max_length=150)
    correct_1 = models.BooleanField(default=False)
    correct_2 = models.BooleanField(default=False)