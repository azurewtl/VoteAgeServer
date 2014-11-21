from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group

# Create your models here.
class User(User):
	userID = models.CharField(primary_key = True, max_length=32)
	userPhone = models.CharField(max_length=32)
	userName = models.CharField(max_length=32)
	userImage = models.CharField(max_length=32)

class VoteFeed(models.Model):
	voteID = models.CharField(primary_key = True, max_length=32)
	voteTitle = models.CharField(max_length=32)
	voteAuthor = models.ForeignKey(User, null = True, blank = True, related_name='voteFeed')
	votePublishDate = models.CharField(max_length=32)
	voteExpireDate = models.CharField(max_length=32)
	voteImage = models.CharField(max_length=32, null = True)


class Option(models.Model):
	voteID = models.ForeignKey(VoteFeed, null = True, blank = True, related_name='option')
	optionTitle = models.CharField(max_length=32)
	menCount = models.IntegerField()
	womenCount = models.IntegerField()

