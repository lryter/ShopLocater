from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',  'name',  'description',  'category',  'pictures',  'coordinatesx',  'coordinatesy',  'rating',  'date_created')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('Username',  'Password')
