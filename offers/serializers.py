from rest_framework import serializers
from .models import Offer

class offerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'