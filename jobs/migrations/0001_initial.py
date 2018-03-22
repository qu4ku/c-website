# Generated by Django 2.0.3 on 2018-03-20 14:42

from django.db import migrations, models
import django.utils.timezone
import jobs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=jobs.models.thirty_days_hence)),
                ('is_active', models.BooleanField(default=False)),
                ('is_payed', models.BooleanField(default=False)),
                ('is_highlighted', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete='CASCADE', to='jobs.Company')),
            ],
        ),
        migrations.CreateModel(
            name='JobTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Job Tag',
                'verbose_name_plural': 'Job Tags',
                'db_table': 'job_tag',
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='job',
            name='tag',
            field=models.ManyToManyField(blank=True, to='jobs.JobTag'),
        ),
    ]