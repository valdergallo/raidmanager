from __future__ import unicode_literals

from django.db import models
from core.models import DifficultType
from core.models import Game


class Raid(models.Model):
    image = models.ImageField(upload_to="/raid/", null=True, blank=True)
    game = models.ForeignKey(Game)
    name = models.CharField(blank=True, max_length=100)
    lvl = models.IntegerField(blank=True, null=True)
    difficult_type = models.ForeignKey(DifficultType)

    def __str__(self):
        return self.name


class Boss(models.Model):
    image = models.ImageField(upload_to="/boss/", null=True, blank=True)
    name = models.CharField(blank=True, max_length=100)
    lvl = models.IntegerField(blank=True, null=True)
    health = models.CharField(blank=True, max_length=100)
    difficult_type = models.ForeignKey(DifficultType)

    def __str__(self):
        return self.name


class RaidGroupAvaliable(models.Model):
    game = models.ForeignKey(Game)
    raid = models.ForeignKey(Raid)
    boss = models.ForeignKey(Boss)
    difficult_type = models.ForeignKey(DifficultType)
    raid_group = models.ForeignKey('RaidGroup')
    status = models.BooleanField(default=False)
    execution_date = models.DateField(null=True, blank=True)


class RaidGroup(models.Model):
    image = models.ImageField(upload_to="/raid_group/", null=True, blank=True)
    game = models.ForeignKey(Game)
    name = models.CharField(blank=True, max_length=100)
    raids = models.ManyToManyField(Raid, through='RaidGroupAvaliable')

    def __str__(self):
        return self.name
