from django.db import models

# Model that contains all the properties for a task.
class Task(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=100, default='')
    created_on = models.CharField(default='')
    priority = models.CharField(max_length=10, default='')
    started = models.BooleanField(default=True)
    started_on = models.CharField(default='')
    completed = models.BooleanField(default=False)
    completed_on = models.CharField(default='')


