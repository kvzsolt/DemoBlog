# Generated by Django 4.0.6 on 2022-07-28 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_slug_alter_post_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AddField(
            model_name='post',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
    ]
