# Generated by Django 3.2.9 on 2021-11-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20211116_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='article_body',
            field=models.TextField(default=0),
        ),
    ]
