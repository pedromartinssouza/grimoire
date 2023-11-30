"""
Definition of models.
"""

from django.db import models


# Create your models here.

class Card(models.Model):
    """
    A playing card.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    manaCost = models.CharField(max_length=100)
    cmc = models.IntegerField()
    colors = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    supertypes = models.CharField(max_length=100)
    subtypes = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)
    text = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class DeckIndex(models.Model):
    """
    A representation for a deck of cards.
    """
    FORMAT_CHOICES = (
        (
            ('Standard', 'Standard'),
            ('Modern', 'Modern'),
            ('Legacy', 'Legacy'),
            ('Vintage', 'Vintage'),
            ('Commander', 'Commander'),
            ('Pauper', 'Pauper'),
            ('Pioneer', 'Pioneer'),
            ('Brawl', 'Brawl'),
            ('Historic', 'Historic'),
            ('Penny', 'Penny'),
            ('Duel', 'Duel'),
            ('Old School', 'Old School'),
            ('Other', 'Other'),
        )
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    format = models.CharField(max_length=100, choices=FORMAT_CHOICES)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class DeckCard(models.Model):
    """
    A representation all cards in relation to a deck.
    """
    id = models.AutoField(primary_key=True)
    deckId = models.ForeignKey(DeckIndex, on_delete=models.CASCADE)
    cardId = models.ForeignKey(Card, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['deckId', 'cardId'], name='unique_deck_card')
        ]
        ordering = ['deckId']

    def __str__(self):
        return self.deckId
