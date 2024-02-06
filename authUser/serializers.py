from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'contact', 'avatar', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'username' in validated_data:
            instance.username = validated_data.get('username', instance.username)
        if 'email' in validated_data:
            instance.email = validated_data.get('email', instance.email)
        if 'contact' in validated_data:
            instance.contact = validated_data.get('contact', instance.contact)
        if 'avatar' in validated_data:
            instance.avatar = validated_data.get('avatar')
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
