# Generated by Django 4.0.2 on 2022-06-10 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='last_name',
        ),
    ]
