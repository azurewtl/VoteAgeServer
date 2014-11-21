from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group

# Create your models here.
class VoteFeed(models.Model):
	voteID = models.CharField(primary_key = True, max_length=32)
	voteTitle = models.CharField(max_length=32)
	voteAuthor = models.CharField(max_length=32)
	voteDate = models.CharField(max_length=32)
	voteImage = models.CharField(max_length=32)


class Option(models.Model):
	voteID = models.ForeignKey(VoteFeed, null = True, blank = True, related_name='option')
	optionTitle = models.CharField(max_length=32)
	menCount = models.IntegerField()
	womenCount = models.IntegerField()

