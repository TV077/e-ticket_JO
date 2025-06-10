from django.shortcuts import render

from rest_framework import viewsets
from .models import Offer
from .serializers import OfferSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
#ModelViewSet fournit automatiquement GET,POST,PUT,DELETE
class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [AllowAny]  #Autorisation

