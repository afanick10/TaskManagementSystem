from django.db import models

# Model that contains all the properties for a task.
# The Task model is used to store user input from
# a modal on the home page to the PostgreSQL database
# and retrieve the data from the database to display 
# all tasks in the table.
class Task(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=100, default='')
    created_on = models.CharField(default='')
    priority = models.CharField(max_length=10, default='')
    started = models.BooleanField(default=False)
    started_on = models.CharField(default='')
    completed = models.BooleanField(default=False)
    completed_on = models.CharField(default='')


