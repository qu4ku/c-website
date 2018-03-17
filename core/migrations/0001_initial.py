# Generated by Django 2.0.3 on 2018-03-17 02:10

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


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
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=60, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=165, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'title',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='DifficultyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty_level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, null=True)),
                ('url', models.URLField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=280)),
                ('slug', models.SlugField(max_length=280, unique_for_date='publish')),
                ('url', models.URLField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('set_number', models.CharField(max_length=2)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('public', 'Public')], default='draft', max_length=20)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('tease', models.CharField(blank=True, help_text='Concise text suggested. Does not appear in RSS feed.', max_length=280)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('seo_title', models.CharField(blank=True, max_length=60, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=165, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('original_author', models.CharField(blank=True, max_length=250)),
                ('original_author_handle', models.CharField(blank=True, max_length=250)),
                ('original_author_url', models.URLField(blank=True, max_length=250)),
                ('thumb_image', models.ImageField(blank=True, upload_to='thumbs/')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete='SET_DEFAULT', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(blank=True, to='core.Category')),
                ('difficulty_level', models.ForeignKey(on_delete='SET_DEFAULT', to='core.DifficultyLevel')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'posts',
                'ordering': ('-publish',),
                'get_latest_by': 'publish',
            },
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('article', 'Article'), ('twitter', 'Twitter'), ('video', 'Video'), ('podcast', 'Podcast')], default='article', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(on_delete='SET_DEFAULT', to='core.PostType'),
        ),
    ]
