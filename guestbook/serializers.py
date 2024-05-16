from rest_framework import serializers
from .models import *

class GuestBookSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = GuestBook
        fields = "__all__"