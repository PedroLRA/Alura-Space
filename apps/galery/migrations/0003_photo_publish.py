# Generated by Django 5.0.4 on 2024-04-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0002_photo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
