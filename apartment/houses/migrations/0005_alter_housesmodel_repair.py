# Generated by Django 5.0 on 2023-12-07 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0004_alter_housesmodel_images_alter_housesmodel_repair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housesmodel',
            name='repair',
            field=models.BooleanField(default=False, verbose_name='Repaire'),
        ),
    ]
