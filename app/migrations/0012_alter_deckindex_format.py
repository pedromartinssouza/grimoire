# Generated by Django 4.2.7 on 2023-11-30 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_card_id_alter_deckindex_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deckindex',
            name='format',
            field=models.CharField(choices=[('Standard', 'Standard'), ('Modern', 'Modern'), ('Legacy', 'Legacy'), ('Vintage', 'Vintage'), ('Commander', 'Commander'), ('Pauper', 'Pauper'), ('Pioneer', 'Pioneer'), ('Brawl', 'Brawl'), ('Historic', 'Historic'), ('Penny', 'Penny'), ('Duel', 'Duel'), ('Old School', 'Old School'), ('Other', 'Other')], max_length=100),
        ),
    ]
