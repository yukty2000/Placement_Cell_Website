# Generated by Django 3.2.5 on 2022-06-10 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='yearOfpassing',
            field=models.IntegerField(default=0),
        ),
    ]
