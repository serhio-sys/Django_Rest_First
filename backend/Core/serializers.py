from . import models
from rest_framework import serializers
from rest_framework.fields import CharField,EmailField
from django.contrib.auth import get_user_model

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=False,use_url=True)
    
    class Meta:
        model = models.Contact
        fields = (
            'id',
            'image',
            'name',
            'email',
            'message',
            'user_id'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"