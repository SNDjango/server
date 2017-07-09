from django.contrib.auth.models import User
from .models import ContentItem, Profile, Comment, Hashtag, ContentHashTag, Like
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'email', 'last_name', 'first_name')

    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'url', 'user', 'personal_info', 'job_title', 'department', 'location', 'expertise',
                  'phone_number', 'contact_skype', 'contact_facebook', 'contact_linkedin', 'user_photo')


class ContentItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentItem
        fields = ('id', 'url', 'upload_date', 'title', 'description', 'image', 'uploaded_by')
        extra_kwargs = {'image': {'required': 'True'}}

    def create(self, validated_data):
        return ContentItem.objects.create(**validated_data)


class HashtagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('id', 'url', 'hashtag_text')


class ContentHashtagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentHashTag
        fields = ('id', 'url', 'content_id', 'hashtag_id')


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'url', 'user_id', 'content_id')
     
    validators = [
        UniqueTogetherValidator(
            queryset=Like.objects.all(),
            fields=('user_id', 'content_id')
        )
    ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'url', 'comment_text', 'publication_date', 'author', 'contentItem')
