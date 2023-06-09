# Generated by Django 4.1.7 on 2023-03-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0002_rename_url_randomurl_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url_name', models.URLField(max_length=250)),
                ('custom_url_name', models.URLField(max_length=250)),
            ],
        ),
    ]
