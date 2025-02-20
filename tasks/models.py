from django.db import models

# Create your models here.
class Task (models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("progress", "Progress"),
        ("completed", "Completed"),
    ]

    title = models.fields.CharField(max_length=100, help_text='What is the name of your task?')
    description = models.fields.TextField(max_length=300, help_text='Describe what the task is')
    creation_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return self.title