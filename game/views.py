from django.shortcuts import render, redirect
from .models import Game
from .forms import GuessNumberForm
import random

def game_view(request):
    message = ''
    game = Game.objects.last()

    if request.method == 'POST':
        form = GuessNumberForm(request.POST)
        if form.is_valid():
            guessed_number = form.cleaned_data['guessed_number']
            game.attempts += 1
            game.save()

            if guessed_number == game.secret_number:
                game.attempts = 0
                game.save()
                return render(request, 'game_over.html')
            elif guessed_number > game.secret_number:
                message += f'Загаданное число меньше чем {guessed_number}'
            else: 
                message += f'Загаданное число больше чем {guessed_number}'
    else:
        form = GuessNumberForm()
        game = Game.objects.create(secret_number=random.randint(1, 100), attempts=0)
    return render(request, 'game.html', {'form': form, 'message': message})