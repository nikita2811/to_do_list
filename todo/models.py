from django.db import models
from django.utils.timezone import now

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
