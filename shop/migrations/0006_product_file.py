# Generated by Django 2.2.10 on 2020-02-23 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(db_index=True, default=10, upload_to=''),
            preserve_default=False,
        ),
    ]
