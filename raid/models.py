from __future__ import unicode_literals

from django.db import models


class Game(models.Model):
    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.names


class RaidType(models.Model):
    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


class Raid(models.Model):
    name = models.CharField(blank=True, max_length=100)
    lvl = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey(RaidType)

    def __str__(self):
        return self.name


class BossType(models.Model):
    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


class Boss(model.Model):
    image = models.ImageField(upload_to="/boss/", null=True, blank=True)
    name = models.CharField(blank=True, max_length=100)
    lvl = models.IntegerField(blank=True, null=True)
    health = models.CharField(blank=True, max_length=100)
    type = models.ForeignKey(BossType)

    def __str__(self):
        return self.name
