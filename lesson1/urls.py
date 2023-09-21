
from django.contrib import admin
from django.urls import path
from sincalc.views import *
from game.views  import *
from HelpDesk.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sin-calc/', sin_calculator, name='sin_calculator'),
    path('game/', game_view, name='game_view'),
    path('help-desk/', desk, name='desk'),
    path('help-desk/<int:pk>/', request_detail, name='request_detail'),
    path('help-desk/registration', registration, name='registration'),
    path('help-desk/login', login, name='login'),
    path('help-desk/logout', logout, name='logout')
]