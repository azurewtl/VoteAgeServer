from django.contrib import admin
from VoteAgeApp.models import VoteFeed, Option

class VoteFeedAdmin(admin.ModelAdmin):
    list_display = ('voteID', 'voteTitle', 'voteImage', 'voteAuthor', 'votePublishDate', 'voteExpireDate')
    search_fields = (['voteID'])

class OptionAdmin(admin.ModelAdmin):
    list_display = ('voteID', 'optionTitle', 'optionImage', 'menCount', 'womenCount')

admin.site.register(VoteFeed, VoteFeedAdmin)
admin.site.register(Option, OptionAdmin)