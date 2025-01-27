# Generated by Django 5.1.1 on 2024-11-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='', unique_for_date='created_at'),
            preserve_default=False,
        ),
    ]
