from django.contrib import admin
from VoteAgeApp.models import VoteFeed, Option

class VoteFeedAdmin(admin.ModelAdmin):
    list_display = ('ID', 'title', 'image', 'author', 'hasVoted', 'publishDate', 'expireDate','latitude', 'longitude')
    search_fields = (['ID'])

class OptionAdmin(admin.ModelAdmin):
    list_display = ('voteID', 'title', 'image', 'menCount', 'womenCount')

admin.site.register(VoteFeed, VoteFeedAdmin)
admin.site.register(Option, OptionAdmin)