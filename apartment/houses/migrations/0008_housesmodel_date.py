# Generated by Django 4.2.7 on 2023-12-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0007_rename_images_housesmodel_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='housesmodel',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
    ]
