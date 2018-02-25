# Generated by Django 2.0.1 on 2018-02-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='seo_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='set_number',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='thumb_image',
            field=models.ImageField(blank=True, upload_to='thumbs/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='original_author_url',
            field=models.URLField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(max_length=250),
        ),
    ]
