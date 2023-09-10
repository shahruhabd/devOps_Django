from django import forms

class GuessNumberForm(forms.Form):
    guessed_number = forms.IntegerField(label='Ваше число', min_value=1, max_value=100)