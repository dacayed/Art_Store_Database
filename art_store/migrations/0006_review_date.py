# Generated by Django 5.1.3 on 2024-12-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_store', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(default="2024-12-10"),
        ),
    ]
