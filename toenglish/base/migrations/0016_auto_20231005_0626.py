# Generated by Django 3.0 on 2023-10-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
