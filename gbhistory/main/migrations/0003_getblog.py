# Generated by Django 5.1.6 on 2025-02-22 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_blogcollect_blog_blog_blogcollect_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.blog')),
            ],
        ),
    ]
