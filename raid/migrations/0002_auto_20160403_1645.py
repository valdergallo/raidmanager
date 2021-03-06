# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raid',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='/raid/'),
        ),
        migrations.AddField(
            model_name='raidgroup',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='/raid_group/'),
        ),
        migrations.AlterField(
            model_name='boss',
            name='difficult_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DifficultType'),
        ),
        migrations.AlterField(
            model_name='raid',
            name='difficult_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DifficultType'),
        ),
        migrations.AlterField(
            model_name='raid',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Game'),
        ),
        migrations.AlterField(
            model_name='raidgroup',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Game'),
        ),
        migrations.AlterField(
            model_name='raidgroupavaliable',
            name='difficult_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DifficultType'),
        ),
        migrations.AlterField(
            model_name='raidgroupavaliable',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Game'),
        ),
        migrations.DeleteModel(
            name='DifficultType',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
