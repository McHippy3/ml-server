from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from json import loads
import pandas as pd
import matplotlib as mpl
from .rossmann_forecast import forecast

@api_view(['POST'])
def load_data(request):
    rossmann_data = pd.read_csv('./time_series/rossmann-data/train.csv', dtype={'StateHoliday':str, 'SchoolHoliday':str})
    for index, row in rossmann_data.iterrows():
        row = Rossmann_Sales(store=row['Store'], dayofweek=row['DayOfWeek'], date=str(row['Date']), sales=row['Sales'], customers=row['Customers'], open=row['Open'], promo=row['Promo'], stateholiday=row['StateHoliday'], schoolholiday=row['SchoolHoliday'])
        row.save()
    return HttpResponse('Data loaded successfully into database')

@api_view(['POST'])
def run_forecast(request):
    forecast()
    return JsonResponse({'Status':'Success'})