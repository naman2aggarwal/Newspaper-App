# Generated by Django 2.1 on 2018-11-28 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
    ]
