# Generated by Django 2.0.3 on 2018-04-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='difficulty_level',
            field=models.ForeignKey(default=0, on_delete='SET_DEFAULT', to='core.DifficultyLevel'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(default=0, on_delete='SET_DEFAULT', to='core.PostType'),
        ),
    ]