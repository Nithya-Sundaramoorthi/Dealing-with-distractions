# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-02 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0002_auto_20160305_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together=set([('question', 'choice_no')]),
        ),
    ]
