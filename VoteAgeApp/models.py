from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
from datetime import datetime, timedelta


def default_expireDate():
	delta = timedelta(days=7)
	return datetime.now() + delta

class User(User):
	userID = models.AutoField(primary_key=True)
	userPhone = models.CharField(max_length=32)
	userName = models.CharField(max_length=32)
	userImage = models.ImageField(upload_to='userImage', null = True, blank = True)


class VoteFeed(models.Model):
	ID = models.AutoField(primary_key=True)
	title = models.CharField(max_length=32)
	image = models.ImageField(upload_to='voteImage', null=True, blank=True)
	author = models.CharField(max_length=32)
	longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
	latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
	publishDate = models.DateTimeField(auto_now=True, blank = True)
	expireDate = models.DateTimeField(default=default_expireDate, blank=True)



class Option(models.Model):
	voteID = models.ForeignKey(VoteFeed, null=True, blank=True, related_name='option')
	title = models.CharField(max_length=32)
	image = models.ImageField(upload_to='optionImage', null=True, blank=True)
	menCount = models.IntegerField(default=0, blank=True)
	womenCount = models.IntegerField(default=0, blank=True)
	longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
	latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
