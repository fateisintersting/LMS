
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

class CourseClass(models.Model):
    course_name = models.CharField(max_length=100)  # The name of the course/class
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)  # References the teacher who created the class
    image = models.ImageField(upload_to='class_images/', blank=True, null=True)  # Optional image for the class
    passkey = models.CharField(max_length=50, unique=True)  # Unique passkey for class access
    description = models.TextField(blank=True, null=True)  # Optional class description
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set the date/time when a class is created
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Auto-generated unique identifier
    
    
class JoinedClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_class = models.ForeignKey(CourseClass, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'course_class')     


class ClassContent(models.Model):
    course_class = models.ForeignKey(CourseClass, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    
class ContentInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey('ClassContent', on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_marked_as_read = models.BooleanField(default=False)
    
    def duration(self):
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds() / 60  # in minutes
        return None    