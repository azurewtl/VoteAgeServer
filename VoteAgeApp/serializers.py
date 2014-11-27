from django.contrib.auth.models import User, Group
from VoteAgeApp.models import VoteFeed, Option
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = ('voteID', 'optionTitle', 'optionImage', 'menCount', 'womenCount')


class VoteFeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VoteFeed
        fields = ('voteID', 'voteTitle', 'voteImage', 'voteAuthor', 'votePublishDate', 'voteExpireDate','option')
        depth = 1



