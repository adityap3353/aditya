from rest_framework import serializers
from .models import *


class aserializer(serializers.ModelSerializer):

    class Meta:
        model = FamilyInfo
        fields = "__all__"
