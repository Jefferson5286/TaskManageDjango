import uuid

from django.db import models


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    finished_at = models.DateField(null=True, blank=True)
