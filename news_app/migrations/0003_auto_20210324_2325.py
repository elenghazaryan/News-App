# Generated by Django 3.1.7 on 2021-03-24 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='detail',
            new_name='content',
        ),
    ]
