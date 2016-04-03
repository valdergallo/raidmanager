from __future__ import unicode_literals

from django.db import models

class Server(models.Model):
    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    image = models.ImageField(upload_to="/game/", null=True, blank=True)
    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


class Faction(models.Model):
    image = models.ImageField(upload_to="/faction/", null=True, blank=True)
    name = models.CharField(blank=True, max_length=100)
    game = models.ForeignKey(Game)

    def __str__(self):
        return self.name


class DifficultType(models.Model):
    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


class SpecType(models.Model):
    action = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.action
