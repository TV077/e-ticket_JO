from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    uuid_key = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
