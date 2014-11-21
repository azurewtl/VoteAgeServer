# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('optionTitle', models.CharField(max_length=32)),
                ('menCount', models.IntegerField()),
                ('womenCount', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteFeed',
            fields=[
                ('voteID', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('voteTitle', models.CharField(max_length=32)),
                ('voteAuthor', models.CharField(max_length=32)),
                ('voteDate', models.CharField(max_length=32)),
                ('voteImage', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='option',
            name='voteID',
            field=models.ForeignKey(related_name='option', blank=True, to='VoteAgeApp.VoteFeed', null=True),
            preserve_default=True,
        ),
    ]
