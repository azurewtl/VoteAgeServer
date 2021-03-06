from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
from datetime import datetime, timedelta


def default_expireDate():
	delta = timedelta(days=7)
	return datetime.now() + delta

class Vote(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=32)
	image = models.ImageField(upload_to='voteImage', null=True, blank=True)
	author = models.CharField(max_length=32)
	hasVoted = models.BooleanField(default=False)
	longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
	latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
	publishDate = models.DateTimeField(auto_now=True, blank = True)
	expireDate = models.DateTimeField(default=default_expireDate, blank=True)

class Option(models.Model):
	voteID = models.ForeignKey(Vote, null=True, blank=True, related_name='option')
	title = models.CharField(max_length=32)
	image = models.ImageField(upload_to='optionImage', null=True, blank=True)
	menCount = models.IntegerField(default=0, blank=True)
	womenCount = models.IntegerField(default=0, blank=True)
