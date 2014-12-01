from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from VoteAgeApp.models import VoteFeed, Option
import VoteAgeApp.serializers as serializers
from django.http import HttpResponse 


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class VoteFeedViewSet(viewsets.ModelViewSet):
    queryset = VoteFeed.objects.all()
    serializer_class = serializers.VoteFeedSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = serializers.OptionSerializer

def test(request):
    print request
    return HttpResponse(request.REQUEST)
