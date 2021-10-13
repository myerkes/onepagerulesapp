# Generated by Django 3.2.4 on 2021-10-13 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('armyapp', '0003_auto_20211013_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialRuleValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('specialrule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armyapp.specialrule')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armyapp.unit')),
            ],
        ),
    ]
