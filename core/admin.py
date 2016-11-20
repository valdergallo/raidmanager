# encoding: utf-8
from django.contrib import admin

from .models import Server
from .models import Game
from .models import Faction
from .models import DifficultType
from .models import SpecType

admin.site.register(Server)
admin.site.register(Game)
admin.site.register(Faction)
admin.site.register(DifficultType)
admin.site.register(SpecType)
