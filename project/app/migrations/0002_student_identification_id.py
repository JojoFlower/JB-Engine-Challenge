# Generated by Django 2.1 on 2018-09-06 21:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='identification_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]