# Generated by Django 2.0.1 on 2018-02-19 23:24

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'title',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='DifficultyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dificulty_level', models.IntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Advanced')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique_for_date='publish')),
                ('url', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('tease', models.TextField(blank=True, help_text='Concise text suggested. Does not appear in RSS feed.')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Public')], default=0)),
                ('publish', models.DateTimeField(default=datetime.datetime.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete='SET_DEFAULT', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(blank=True, to='pages.Category')),
                ('difficulty_level', models.ForeignKey(on_delete='SET_DEFAULT', to='pages.DifficultyLevel')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'db_table': 'posts',
                'ordering': ('-publish',),
                'get_latest_by': 'publish',
            },
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.IntegerField(choices=[(0, 'Article'), (1, 'Twitter'), (2, 'Video')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(on_delete='SET_DEFAULT', to='pages.PostType'),
        ),
    ]
