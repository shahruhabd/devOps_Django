
from django.contrib import admin
from django.urls import path
from sincalc.views import *
from game.views  import *

urlpatterns = [
    path('', sin_calculator, name='sin_calculator'),
    path('game/', game_view, name='main_page'),
    path('admin/', admin.site.urls),
]