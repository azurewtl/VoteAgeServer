from django.contrib import admin
from VoteAgeApp.models import VoteFeed, Option

class VoteFeedAdmin(admin.ModelAdmin):
    list_display = ('ID', 'title', 'image', 'author', 'publishDate', 'expireDate','latitude', 'longitude', 'option')
    search_fields = (['voteID'])

class OptionAdmin(admin.ModelAdmin):
    list_display = ('voteID', 'title', 'image', 'menCount', 'womenCount', 'latitude', 'longitude')

admin.site.register(VoteFeed, VoteFeedAdmin)
admin.site.register(Option, OptionAdmin)