from dataclasses import fields
from todoapi.serializers import *
from todoapi.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'