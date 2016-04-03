from __future__ import unicode_literals

from django.db import models


class Server(models.Model):
    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


class SpecType(models.Model):
    action = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.action


class Specs(models.Model):
    image = models.ImageField(upload_to="/specs/", null=True, blank=True)
    name = models.CharField(blank=True, max_length=100)
    spec_type = models.ForeignKey(SpecType)

    def __str__(self):
        return self.name


class Classes(models.Model):
    image = models.ImageField(upload_to="/classes/", null=True, blank=True)
    name = models.CharField(blank=True, max_length=100)
    color = models.CharField(blank=True, max_length=100)
    specs = models.ManyToManyField(Specs)

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

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(blank=True, max_length=100)
    game = models.ForeignKey(Game)
    faction = models.ForeignKey(Faction)

    def __str__(self):
        return self.name


class Player(models.Model):
    image = models.ImageField(upload_to="/player/%Y/%m/%d/", null=True, blank=True)
    name = models.CharField(blank=True, max_length=100)
    ilvl = models.IntegerField(blank=True, null=True)
    lvl = models.IntegerField(blank=True, null=True)
    race = models.ForeignKey(Race)
    server = models.ForeignKey(Server)
    classe = models.ForeignKey(Classes)
    main_spec = models.ForeignKey(Specs)
    off_spec = models.ForeignKey(Specs)
    creation_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{name} {ilvl}'.format(self.name, self.ilvl)
