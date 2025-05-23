# Generated by Django 5.2.1 on 2025-05-16 00:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


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
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('apellido', models.CharField(blank=True, max_length=100)),
                ('avatar', models.ImageField(blank=True, default='avatars/default.png', upload_to='avatars/')),
                ('biografia', models.TextField(blank=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
