# Generated by Django 5.1.4 on 2025-01-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_categories_image_alter_products_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
