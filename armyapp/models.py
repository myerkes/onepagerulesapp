from django.db import models

# Create your models here.
class SpecialRule(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    value = models.IntegerField

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    range = models.IntegerField
    attacks = models.IntegerField
    specialrules = models.ManyToManyField(SpecialRule)

class UpgradeListItems(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField

class Upgrade(models.Model):
    name = models.CharField(max_length=255)
    upgradelistitems = models.ManyToManyField(UpgradeListItems)

class PsychicSpell(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    quality = models.IntegerField

class Unit(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField
    quality = models.IntegerField
    defense = models.IntegerField
    cost = models.IntegerField
    equipments = models.ManyToManyField(Equipment)
    specialrules = models.ManyToManyField(SpecialRule)
    upgrades = models.ManyToManyField(Upgrade)

class Army(models.Model):
    name = models.CharField(max_length=255)
    background = models.CharField(max_length=1000)
    units = models.ManyToManyField(Unit)
    specialrules = models.ManyToManyField(SpecialRule)
    upgrades = models.ManyToManyField(Upgrade)
    pyschicspells = models.ManyToManyField(PsychicSpell)
