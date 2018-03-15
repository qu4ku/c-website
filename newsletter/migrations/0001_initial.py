# Generated by Django 2.0.3 on 2018-03-15 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('date_subscribed', models.DateTimeField(auto_now_add=True)),
                ('date_unsubscribed', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Newsletter Contact',
                'verbose_name_plural': 'Newsletter Contacts',
                'db_table': 'newsletter_contacts',
                'ordering': ('-date_subscribed',),
            },
        ),
    ]
