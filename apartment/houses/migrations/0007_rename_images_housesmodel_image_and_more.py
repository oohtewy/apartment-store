# Generated by Django 5.0 on 2023-12-10 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0006_housesmodel_image_height_housesmodel_image_width'),
    ]

    operations = [
        migrations.RenameField(
            model_name='housesmodel',
            old_name='images',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='housesmodel',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='housesmodel',
            name='image_width',
        ),
        migrations.RemoveField(
            model_name='housesmodel',
            name='repair',
        ),
    ]