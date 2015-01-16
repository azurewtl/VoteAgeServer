from django.contrib import admin
import models

class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'author', 'hasVoted', 'publishDate', 'expireDate','latitude', 'longitude')
    search_fields = (['id'])

class OptionAdmin(admin.ModelAdmin):
    list_display = ('voteID', 'title', 'image', 'menCount', 'womenCount')

admin.site.register(models.Vote, VoteAdmin)
admin.site.register(models.Option, OptionAdmin)