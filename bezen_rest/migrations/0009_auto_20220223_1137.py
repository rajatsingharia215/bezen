# Generated by Django 3.0.5 on 2022-02-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bezen_rest', '0008_auto_20220222_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedFish',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img_name', models.CharField(max_length=150)),
                ('is_Resized', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='fish',
            name='timestamp',
            field=models.DateTimeField(default='2022-02-23 11:37:44'),
        ),
    ]
