# Generated by Django 3.0.6 on 2020-05-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200519_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
