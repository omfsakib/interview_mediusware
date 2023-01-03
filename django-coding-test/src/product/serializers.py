from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        models = Product
        fields = '__all__'