# Generated by Django 5.1 on 2024-08-25 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_researchpaper_user_alter_researchpaper_authors_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
