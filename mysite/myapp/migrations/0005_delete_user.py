# Generated by Django 3.2.9 on 2021-11-15 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_user_name_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
