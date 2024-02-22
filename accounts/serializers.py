from rest_framework import serializers 
from .models import *


class SerializerPeofile(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = "__all__"

 