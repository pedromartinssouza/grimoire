# Generated by Django 2.2.28 on 2023-11-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='releaseDate',
        ),
        migrations.AlterField(
            model_name='card',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
