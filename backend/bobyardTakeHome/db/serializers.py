from rest_framework import serializers
from db.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'parent', 'text', 'date', 'likes', 'image']
