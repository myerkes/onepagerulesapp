from armyapp.models import Unit
from django.contrib import admin
from .models import SpecialRule, Equipment, UpgradeListItems, Upgrade, PsychicSpell, Unit, Army, SpecialRuleUnitJoin

# Register your models here.
admin.site.register(SpecialRule)
admin.site.register(Equipment)
admin.site.register(UpgradeListItems)
admin.site.register(Upgrade)
admin.site.register(PsychicSpell)
admin.site.register(Unit)
admin.site.register(Army)
admin.site.register(SpecialRuleUnitJoin)