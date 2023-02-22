import uuid
from django.db import models


# Create your models here.
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    status = models.BooleanField(default=False)
    dueDate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tasks"
        ordering = ["dueDate"]

        def __str__(self) -> str:
            return self.title
