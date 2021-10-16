# Generated by Django 3.2.8 on 2021-10-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20211016_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='memberships',
            new_name='membership',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='given_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]