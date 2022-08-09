from rest_framework.serializers import ModelSerializer
from todo.models import Todos
from rest_framework import serializers
from django.contrib.auth.models import User

class TodoSerializer(ModelSerializer):
    user=serializers.CharField(read_only=True)
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Todos
        fields=['id','task_name','user','status',]
    def create(self, validated_data):
        user=self.context.get('user')
        return Todos.objects.create(**validated_data,user=user)



class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']


    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()