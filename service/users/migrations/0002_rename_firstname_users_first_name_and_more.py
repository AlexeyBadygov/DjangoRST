# Generated by Django 4.0.2 on 2022-04-22 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
