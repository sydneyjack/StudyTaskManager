
from django.db import models


class Task(models.Model):
    """Store a student's study task and its completion status."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the task title for display."""
        return self.title
