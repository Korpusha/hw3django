# Generated by Django 3.2.9 on 2021-11-16 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20211115_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('do_you_like_it', models.BooleanField(verbose_name='Do you like it?')),
                ('article_name', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_user_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='amount',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='myapp.author'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('do_you_like_it', models.BooleanField(verbose_name='Do you like it?')),
                ('comment', models.TextField()),
                ('blog_blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapp.blog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='myapp.bloguser'),
        ),
    ]
