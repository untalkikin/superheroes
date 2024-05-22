from .models import Hero
from rest_framework import serializers

class HeroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields ='__all__'