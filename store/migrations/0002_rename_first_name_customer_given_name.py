# Generated by Django 3.2.7 on 2021-10-16 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='given_name',
        ),
    ]