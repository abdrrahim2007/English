# Generated by Django 3.0 on 2023-08-24 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_story_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversations',
            name='conversations',
        ),
        migrations.AddField(
            model_name='conversation',
            name='conversation',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base.Conversations'),
            preserve_default=False,
        ),
    ]
