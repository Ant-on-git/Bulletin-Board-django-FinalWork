# Generated by Django 4.2 on 2023-05-16 10:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0003_alter_onetimecode_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='accepted',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(-1)]),
        ),
    ]
