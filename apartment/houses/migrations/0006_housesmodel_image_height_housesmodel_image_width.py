# Generated by Django 5.0 on 2023-12-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0005_alter_housesmodel_repair'),
    ]

    operations = [
        migrations.AddField(
            model_name='housesmodel',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='housesmodel',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]