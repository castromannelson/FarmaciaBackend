from rest_framework import serializers
from .models import UserAccount

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserAccount
        fields = [
            'id',
            'name',
            'lastNames',
            'rol',
            'username',
            'password'
        ]
        
    def create(self, validated_data):
        user = UserAccount.objects.create(**validated_data)
        
        user.set_password(user.password) #Encriptar/hashear password
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        if password:
            instance.set_password(password)
        
        return super().update(instance, validated_data)