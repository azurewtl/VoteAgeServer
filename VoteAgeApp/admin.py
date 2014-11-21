from django.contrib import admin
from VoteAgeApp.models import VoteFeed, Option

class VoteFeedAdmin(admin.ModelAdmin):
    list_display = ('voteID', 'voteTitle', 'voteAuthor', 'votePublishDate', 'voteImage' )
    search_fields = (['voteID'])

class OptionAdmin(admin.ModelAdmin):
    list_display = ('voteID', 'optionTitle', 'menCount', 'womenCount')

admin.site.register(VoteFeed, VoteFeedAdmin)
admin.site.register(Option, OptionAdmin)