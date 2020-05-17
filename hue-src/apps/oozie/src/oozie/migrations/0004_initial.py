# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-06 18:55
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oozie', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinator',
            name='coordinatorworkflow',
            field=models.ForeignKey(help_text='The workflow to schedule repeatedly.', null=True, on_delete=django.db.models.deletion.CASCADE, to='oozie.Workflow', verbose_name='Workflow'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='coordinators',
            field=models.ManyToManyField(through='oozie.BundledCoordinator', to='oozie.Coordinator'),
        ),
    ]
