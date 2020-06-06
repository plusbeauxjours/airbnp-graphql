# Generated by Django 3.1a1 on 2020-06-06 09:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20191216_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]