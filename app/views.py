"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Card
from app.models import DeckIndex
from app.models import DeckCard
from app.forms import CardForm
from app.forms import DeckIndexForm
from app.forms import DeckCardForm
from django.db.models import ProtectedError



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'This beautiful application was created by Luis and Pedro, the coolest guys around.',
            'year': datetime.now().year,
        }
    )


def cards(request):
    """Renders the cards page."""

    cards = Card.objects.all()
    card_id = None
    form = CardForm()
    error = None
    if request.method == 'GET':
        if 'update-id' in request.GET:
            card = Card.objects.get(pk=request.GET['update-id'])
            form = CardForm(instance=card)
            card_id = request.GET['update-id']
    if request.method == 'POST':
        if 'delete-id' in request.POST:
            try:
                Card.objects.get(pk=request.POST['delete-id']).delete()
            except ProtectedError:
                error = "Card is in a deck, cannot delete"
            form = CardForm()
        elif 'update-id' in request.POST:
            card = Card.objects.get(pk=request.POST['update-id'])
            form = CardForm(request.POST, instance=card)
            if form.is_valid():
                form.save()
                form = CardForm()
        else:
            form = CardForm(request.POST)
            if form.is_valid():
                form.save()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cards.html',
        {
            'title': 'Cards',
            'message': 'Register and view cards.',
            'year': datetime.now().year,
            'cards': cards,
            'form': form,
            'id': card_id,
            'operationError': error,
        }
    )


def decks(request):
    """Renders the decks page."""

    decks = DeckIndex.objects.all()
    deck_index_id = None
    form = DeckIndexForm()
    if request.method == 'GET':
        if 'update-id' in request.GET:
            deck_index = DeckIndex.objects.get(pk=request.GET['update-id'])
            form = DeckIndexForm(instance=deck_index)
            deck_index_id = request.GET['update-id']
    if request.method == 'POST':
        if 'delete-id' in request.POST:
            form = DeckIndexForm()
            DeckIndex.objects.get(pk=request.POST['delete-id']).delete()
        elif 'update-id' in request.POST:
            deck_index = DeckIndex.objects.get(pk=request.POST['update-id'])
            form = DeckIndexForm(request.POST, instance=deck_index)
            if form.is_valid():
                form.save()
                form = DeckIndexForm()
        else:
            form = DeckIndexForm(request.POST)
            if form.is_valid():
                form.save()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/decks.html',
        {
            'title': 'Decks',
            'message': 'Register and list decks.',
            'year': datetime.now().year,
            'decks': decks,
            'form': form,
            'id': deck_index_id,
        }
    )


def deck_editor(request):
    """Renders the cards page."""
    deck_index_id = None
    if request.method == 'POST':
        if 'delete-id' in request.POST:
            DeckCard.objects.get(pk=request.POST['delete-id']).delete()
            deck_index_id = request.POST['deck-edit-id']
        elif 'deck-edit-id' in request.POST:
            deck_index_id = request.POST['deck-edit-id']
            form = DeckCardForm(request.POST)
            form.instance.deckId = DeckIndex.objects.get(pk=deck_index_id)
            deck = DeckIndex.objects.get(pk=deck_index_id)
            deck_info = DeckCard.objects.select_related().filter(deckId=deck)
            if form.is_valid():
                form.save()
            return render(
                request,
                'app/deck_editor.html',
                {
                    'title': deck.name,
                    'message': deck.description,
                    'year': datetime.now().year,
                    'decks': decks,
                    'list_of_cards_in_deck': deck_info,
                    'all_cards': Card.objects.all(),
                    'form': form,
                    'id': deck_index_id,
                }
            )
        elif 'delete-card' in request.POST:
            DeckCard.objects.get(pk=request.POST['delete-card']).delete()
    if request.method == 'GET':
        if 'deck-edit-id' in request.GET:
            deck_index_id = request.GET['deck-edit-id']
    form = DeckCardForm()
    deck = DeckIndex.objects.get(pk=deck_index_id)
    deck_info = DeckCard.objects.select_related().filter(deckId=deck)
    return render(
        request,
        'app/deck_editor.html',
        {
            'title': deck.name,
            'message': deck.description,
            'year': datetime.now().year,
            'decks': decks,
            'list_of_cards_in_deck': deck_info,
            'all_cards': Card.objects.all(),
            'form': form,
            'id': deck_index_id,
        }
    )

