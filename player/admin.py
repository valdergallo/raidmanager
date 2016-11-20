# encoding: utf-8
from django.contrib import admin

from .models import Specs
from .models import Classes
from .models import Game
from .models import Faction
from .models import Race
from .models import Player


admin.site.register(Specs)
