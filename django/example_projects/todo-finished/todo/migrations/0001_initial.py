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
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('modified', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('deadline', models.DateField(null=True, blank=True)),
                ('done', models.BooleanField(default=False)),
                ('attachment', models.FileField(null=True, upload_to=b'tasks', blank=True)),
            ],
            options={
                'ordering': ('-deadline',),
                'db_table': 'task',
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'permissions': (('search_task', 'Search task'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('modified', models.DateField(auto_now=True, null=True)),
                ('label', models.CharField(max_length=100)),
                ('users', models.ManyToManyField(related_name='todo_lists', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ('label',),
                'db_table': 'todo_list',
                'verbose_name': 'Todo list',
                'verbose_name_plural': 'Todo lists',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='todo_list',
            field=models.ForeignKey(related_name='tasks', to='todo.TodoList'),
            preserve_default=True,
        ),
    ]
