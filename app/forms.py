"""
Definition of forms.
"""

from django import forms
from app.models import Card, DeckIndex, DeckCard
from django.contrib.auth.forms import AuthenticationForm


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class CardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Card
        fields = '__all__'


class DeckIndexForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeckIndexForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = DeckIndex
        fields = '__all__'


class DeckCardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeckCardForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = DeckCard
        fields = ('cardId', 'quantity')
