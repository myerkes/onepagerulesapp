# Generated by Django 3.2.4 on 2021-10-13 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyapp', '0008_remove_unit_specialrules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialruleunitjoin',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
