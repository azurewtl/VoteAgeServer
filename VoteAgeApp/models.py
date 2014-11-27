from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group



# Create your models here.
class User(User):
	userID = models.AutoField(primary_key = True)
	userPhone = models.CharField(max_length=32)
	userName = models.CharField(max_length=32)
	userImage = models.ImageField(upload_to='userImage', null = True, blank = True)


class VoteFeed(models.Model):
	voteID = models.AutoField(primary_key = True)
	voteTitle = models.CharField(max_length=32)
	voteAuthor = models.CharField(max_length=32)
	votePublishDate = models.DateTimeField(auto_now = True, blank = True)
	voteExpireDate = models.DateTimeField(blank = True)
	voteImage = models.ImageField(upload_to='voteImage', null = True, blank = True)
	def save(self):
		from datetime import datetime, timedelta
		delta = timedelta(days=7)
		if not self.voteID:
			self.voteExpireDate = datetime.now() + delta
			super(VoteFeed, self).save()

class Option(models.Model):
	voteID = models.ForeignKey(VoteFeed, null = True, blank = True, related_name='option')
	optionTitle = models.CharField(max_length=32)
	optionImage = models.ImageField(upload_to='optionImage', null = True, blank = True)
	menCount = models.IntegerField(default = 0)
	womenCount = models.IntegerField(default = 0)
