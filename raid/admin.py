# encoding: utf-8
from django.contrib import admin
from .models import Raid
from .models import Boss
from .models import RaidGroupAvaliable
from .models import RaidGroup


admin.site.register(Raid)
admin.site.register(Boss)
admin.site.register(RaidGroupAvaliable)
admin.site.register(RaidGroup)
