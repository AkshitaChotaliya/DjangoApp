from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='todo_images/', null=True, blank=True)

    
    def __str__(self):
           return self.task