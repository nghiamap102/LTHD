# Generated by Django 3.2.5 on 2021-10-19 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_blog_decription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'like'), (2, 'heart'), (1, 'haha'), (3, 'sad'), (4, 'angry')], default=0),
        ),
    ]
