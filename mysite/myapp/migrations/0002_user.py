# Generated by Django 3.2.9 on 2021-11-15 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_to_buy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='myapp.book')),
            ],
        ),
    ]