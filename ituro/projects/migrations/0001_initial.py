# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_manager', models.BooleanField(default=False, verbose_name='Is project manager?')),
                ('member', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=30, verbose_name='Category', choices=[(b'line_follower', 'Line Follower'), (b'micro_sumo', 'Micro Sumo'), (b'fire_fighter', 'Fire Fighter'), (b'basketball', 'Basketball'), (b'stair_climbing', 'Stair Climbing'), (b'maze', 'Maze'), (b'color_selecting', 'Color Selecting'), (b'self_balancing', 'Self Balancing'), (b'scenario', 'Scenario'), (b'innovative', 'Innovative')])),
                ('name', models.CharField(max_length=50, verbose_name='Project Name')),
                ('presentation', models.FileField(upload_to=b'presentations', verbose_name='Project Presentation File', blank=True)),
                ('design', models.BooleanField(default=False, verbose_name='I want to join Autodesk Digital Design Contest.')),
                ('is_valid', models.BooleanField(default=False, verbose_name='Is project valid?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('category', 'name')]),
        ),
        migrations.AddField(
            model_name='membership',
            name='project',
            field=models.ForeignKey(verbose_name='Project', to='projects.Project'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('member', 'project')]),
        ),
    ]
