# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='/classes/')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('color', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='/faction/')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='/game/')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='/player/%Y/%m/%d/')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('ilvl', models.IntegerField(blank=True, null=True)),
                ('lvl', models.IntegerField(blank=True, null=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Classes')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Faction')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='/specs/')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SpecType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='specs',
            name='spec_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.SpecType'),
        ),
        migrations.AddField(
            model_name='player',
            name='main_spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_spec', to='player.Specs'),
        ),
        migrations.AddField(
            model_name='player',
            name='off_spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='off_spec', to='player.Specs'),
        ),
        migrations.AddField(
            model_name='player',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Race'),
        ),
        migrations.AddField(
            model_name='player',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Server'),
        ),
        migrations.AddField(
            model_name='classes',
            name='specs',
            field=models.ManyToManyField(to='player.Specs'),
        ),
    ]
