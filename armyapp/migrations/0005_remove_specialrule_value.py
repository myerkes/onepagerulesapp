# Generated by Django 3.2.4 on 2021-10-13 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armyapp', '0004_specialrulevalue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialrule',
            name='value',
        ),
    ]
