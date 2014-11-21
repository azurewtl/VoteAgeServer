from django.shortcuts import render
from VoteAgeApp.models import VoteFeed, Option
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from VoteAgeApp.serializers import UserSerializer, GroupSerializer, VoteFeedSerializer, OptionSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class VoteFeedViewSet(viewsets.ModelViewSet):
    queryset = VoteFeed.objects.all()
    serializer_class = VoteFeedSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

