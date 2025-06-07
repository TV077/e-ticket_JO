from django.db import models

# Create your models here.
class Offer(models.Model):
    OFFER_TYPE = [
        ('solo', 'Solo'),
        ('duo','Duo'),
        ('famille', 'Famille'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=OFFER_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name