# Generated by Django 2.2.17 on 2021-02-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20210129_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
