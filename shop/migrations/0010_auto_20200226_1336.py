# Generated by Django 2.2.10 on 2020-02-26 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200226_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category_fb',
            old_name='Категория',
            new_name='Категория fb account',
        ),
        migrations.RenameField(
            model_name='category_offer',
            old_name='Категория',
            new_name='Категория offers',
        ),
    ]
