from django.shortcuts import render
import math
from .models import SinCalculation
from datetime import datetime

def sin_calculator(request):
    if request.method == 'POST':

        angle = float(request.POST.get('angle'))
        result = math.sin(math.radians(angle))
        created_at = datetime.now().time()
        
        calculation = SinCalculation(angle=angle, result=result, created_at=created_at)
        calculation.save()

        return render(request, 'sin_calculator.html', {'result': result})

    return render(request, 'sin_calculator.html')
