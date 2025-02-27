# Generated by Django 5.1.4 on 2025-01-03 20:06

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('active', models.BooleanField(default=False)),
                ('init_date', models.DateField()),
                ('end_date', models.DateField()),
                ('type', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_policies', to=settings.AUTH_USER_MODEL)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker_policies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'indexes': [models.Index(fields=['active'], name='poliza_poli_active_5943d1_idx'), models.Index(fields=['deleted_at'], name='poliza_poli_deleted_5d6c97_idx')],
            },
        ),
    ]
