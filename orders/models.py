from symtable import Class

from django.db import models
from django.conf import settings
from offers.models import Offer
import uuid

# Create your models here.

#Commande d'un utilisateur
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    ticket_key = models.UUIDField(default=uuid.uuid4, editable=False)

#Ticket généré à la suite d'une commande
    def __str__(self):
        return f"Commande de {self.user} - {self.offer.name}"

class Ticket(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    final_key = models.CharField(max_length=255) #clé concaténée  = uuid_user + ticket_key
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"Ticket - {self.order.user.username} - ({'valide' if self.is_valid else 'utilisé'})"
