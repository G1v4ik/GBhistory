# Generated by Django 5.1.6 on 2025-03-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='Просмотров'),
        ),
    ]
