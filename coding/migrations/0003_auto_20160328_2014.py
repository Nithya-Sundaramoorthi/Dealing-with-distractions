# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-28 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0002_auto_20160328_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputcase',
            name='case_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='inputcase',
            unique_together=set([('question', 'case_no')]),
        ),
    ]