# Generated by Django 4.2.4 on 2024-05-05 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proveedor', '0003_post_actualizado_post_creado_alter_post_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='id_proveedor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
