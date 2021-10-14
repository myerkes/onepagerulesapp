from django.db import models

# Create your models here.
class SpecialRule(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    range = models.IntegerField(default=0)
    attacks = models.IntegerField(default=0)
    specialrules = models.ManyToManyField(SpecialRule, blank=True)

    def __str__(self) -> str:
        return self.name

class UpgradeListItems(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class PsychicSpell(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    quality = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField(default=0)
    quality = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    equipments = models.ManyToManyField(Equipment, blank=True)
    upgrades = models.ManyToManyField('Upgrade', blank=True)

    def __str__(self) -> str:
        return self.name

class SpecialRuleUnitJoin(models.Model):
    value = models.IntegerField(blank=True, null=True)
    specialrule = models.ForeignKey(SpecialRule, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self) -> str:
        if self.value:
            return f'{self.specialrule.name}({self.value}) - {self.unit.name }'
        else:
            return f'{self.specialrule.name} - {self.unit.name }'

class Army(models.Model):
    name = models.CharField(max_length=255)
    background = models.CharField(max_length=1000)
    units = models.ManyToManyField(Unit, blank=True, related_name='units')
    specialrules = models.ManyToManyField(SpecialRule, blank=True)
    pyschicspells = models.ManyToManyField(PsychicSpell, blank=True)

    def __str__(self) -> str:
        return self.name

class Upgrade(models.Model):
    name = models.CharField(max_length=255)
    upgradelistitems = models.ManyToManyField(UpgradeListItems, blank=True)
    army = models.ForeignKey(Army, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
