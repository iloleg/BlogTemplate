# Generated by Django 3.0.6 on 2020-05-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200519_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
