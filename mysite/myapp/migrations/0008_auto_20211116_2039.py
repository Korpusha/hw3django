# Generated by Django 3.2.9 on 2021-11-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20211116_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='email',
            field=models.EmailField(default=0, max_length=254),
        ),
        migrations.AddField(
            model_name='bloguser',
            name='password',
            field=models.CharField(default=0, max_length=120),
        ),
    ]
