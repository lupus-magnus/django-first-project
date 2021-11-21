from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    STATUS_CHOICES = (
        ('Planning stage', 'Planning stage 🗒️'),
        ('In development', 'In development ⚙️'),
        ('Up and running', 'Up and running 🌐')
    )
    status = models.CharField(choices=STATUS_CHOICES, default= 'Planning stage', max_length=160)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.title
