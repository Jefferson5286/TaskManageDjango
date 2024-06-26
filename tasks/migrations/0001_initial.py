# Generated by Django 5.0.4 on 2024-04-10 14:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('finished_at', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
