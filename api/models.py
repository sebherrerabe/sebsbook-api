from cgitb import text
from importlib.resources import contents
from django.db import models
import uuid
# Create your models here.


class Post(models.Model):
    uniqueID = models.UUIDField(max_length=255, primary_key=True, default=uuid.uuid4)
    img = models.TextField(max_length=255, blank=True, null=True)
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
