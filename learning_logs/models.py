from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """A topic the user is learning"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of Topic model"""
        return self.text
    

class Entry(models.Model):
    """Something specific learned about the Topic at hand"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='entries')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """define plural for model when referred in admins page"""
        verbose_name_plural = 'Entries'

    def __str__(self) -> str:
        return f"{self.text[:50]}..."