# Generated by Django 4.2.7 on 2023-11-30 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_deckcard_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deckcard',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
