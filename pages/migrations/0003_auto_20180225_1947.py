# Generated by Django 2.0.1 on 2018-02-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180225_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb_image',
            field=models.ImageField(blank=True, null=True, upload_to='thumbs/'),
        ),
    ]