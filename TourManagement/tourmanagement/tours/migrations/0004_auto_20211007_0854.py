# Generated by Django 3.2.5 on 2021-10-07 01:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20211007_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='adult',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='booking',
            name='children',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
