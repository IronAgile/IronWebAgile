# Generated by Django 2.0.2 on 2018-04-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IronAgileWebApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_present',
            field=models.BooleanField(default='1'),
            preserve_default=False,
        ),
    ]