from rest_framework import serializers
from .models import ServerValue

class todobasicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['ID','ValueType','StringValue1','StringValue2','StringValue3']

