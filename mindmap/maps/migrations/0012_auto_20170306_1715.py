# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-06 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0011_auto_20170302_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='type',
            field=models.CharField(choices=[('N', 'Node'), ('T', 'Textbox')], default='N', max_length=50),
        ),
    ]