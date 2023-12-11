# Generated by Django 4.2.7 on 2023-12-11 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField(max_length=50, verbose_name='Name')),
                ('lname', models.TextField(max_length=60, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('image', models.ImageField(default='profiles/default.jpg', upload_to='profiles')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]