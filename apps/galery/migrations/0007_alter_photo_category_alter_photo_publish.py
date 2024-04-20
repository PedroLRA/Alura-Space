# Generated by Django 5.0.4 on 2024-04-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0006_photo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.CharField(choices=[('NEBULA', 'Nebula'), ('STAR', 'Star'), ('GALAXY', 'Galaxy'), ('PLANET', 'Planet')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='photo',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
