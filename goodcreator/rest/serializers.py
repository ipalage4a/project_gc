from goodcreator.models import Entry
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['title']


class EntrySerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Entry
        fields = ['title', 'body', 'category_id']