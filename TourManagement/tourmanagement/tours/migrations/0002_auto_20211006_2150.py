# Generated by Django 3.2.5 on 2021-10-06 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='content',
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='static/user/%Y/%m'),
        ),
    ]