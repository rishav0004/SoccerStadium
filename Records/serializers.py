from dataclasses import field
from rest_framework import serializers
from .models import Players

class PlayerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'
