# Generated by Django 4.0.2 on 2022-04-07 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_project_socials_alter_project_description'),
        ('auth_app', '0005_delete_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='socials',
        ),
        migrations.DeleteModel(
            name='SocialMedia',
        ),
    ]
