# models.py

from django.db import models

class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    instructor_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=50)  # e.g., "3 months"
    created_at = models.DateTimeField(auto_now_add=True)
    short_description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    

    def __str__(self):
        return self.course_name

class Sections(models.Model):
    course = models.ForeignKey(Courses, related_name='sections', on_delete=models.CASCADE)
    section_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.section_name

class Chapter(models.Model):
    section = models.ForeignKey(Sections, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField()

    def __str__(self):
        return self.title
