from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username")
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'post', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field="username",
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        read_only=False, slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        fields = ('id', 'user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]

    def validate(self, data):
        user = self.context["request"].user
        if user == data["following"]:
            raise serializers.ValidationError(
                {"error": "no self following"}
            )
        return data
