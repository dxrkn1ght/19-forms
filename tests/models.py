from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=100)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE, related_name='tests')

    def __str__(self):
        return self.name