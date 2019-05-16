from rest_framework import serializers

from user.models import User
from .models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all())
    title = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Post
        fields = ('id', 'user_id', 'title', 'description')


class PostLikeSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id',)
