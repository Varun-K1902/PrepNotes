from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.TextField()

    def __str__(self):
        return self.title

class Post(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='posts')
    question = models.TextField()
    answer_desc = models.TextField()
    answer = HTMLField()

    def __str__(self):
        return self.question[:50]
