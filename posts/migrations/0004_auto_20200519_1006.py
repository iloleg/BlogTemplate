# Generated by Django 3.0.6 on 2020-05-19 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200519_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_created_on',
            field=models.DateTimeField(default=True),
        ),
    ]
