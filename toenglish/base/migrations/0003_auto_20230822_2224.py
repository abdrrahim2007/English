# Generated by Django 3.0 on 2023-08-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20230822_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Stories',
        ),
    ]
