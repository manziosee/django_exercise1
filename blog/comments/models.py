from django.db import models
from myblog.models import Blog
from django.contrib.auth import get_user_model
user=get_user_model()
import uuid

# Create your models here.
class Comment(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=True)
    