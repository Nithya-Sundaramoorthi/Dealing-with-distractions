# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-02 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0015_auto_20160402_1237'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teammcqanswer',
            unique_together=set([('question_no', 'team')]),
        ),
    ]