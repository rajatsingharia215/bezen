# Generated by Django 3.0.5 on 2022-02-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bezen_rest', '0011_auto_20220223_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='timestamp',
            field=models.DateTimeField(default='2022-02-23 15:11:53'),
        ),
    ]
