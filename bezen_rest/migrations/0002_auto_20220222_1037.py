# Generated by Django 3.0.5 on 2022-02-22 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bezen_rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='timestamp',
            field=models.DateTimeField(default='2022/02/22 10:37:55'),
        ),
    ]
