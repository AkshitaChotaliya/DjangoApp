from django.db import models
from django.contrib import admin
from datetime import datetime


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=datetime.now)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    position = models.PositiveIntegerField()
    video_url = models.URLField(max_length=500)
