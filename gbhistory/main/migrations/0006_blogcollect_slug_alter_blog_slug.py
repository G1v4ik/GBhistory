# Generated by Django 5.1.6 on 2025-02-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcollect',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
