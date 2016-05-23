from rest_framework import serializers
from .models import Task

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',  'name',  'description',  'category',  'pictures',  'coordinatesx',  'coordinatesy',  'rating',  'date_created')
