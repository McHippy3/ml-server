from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from json import loads
import random
from .regression import run_regression

def results(request):
    return render(request, "results.html", {})

@api_view(['GET'])
def generate_data(request):
    length = request.GET.get('length', '100')
    dataset_id = request.GET.get('dataset_id', '')
    unit = request.GET.get('unit', 'unit')
    try:
        for i in range(int(length)):
            value = 0.3 * i + 5 + random.uniform(-0.5,0.5)
            newData = Data(dataset_id=int(dataset_id), forecasting_unit=unit, time_period=str(i), value=value)
            newData.save()
    except:
        return JsonResponse({'status':'failure, one or more fields missing/invalid'}, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({'status':'data created'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def generate_sku_history(request):
    sku_codes = ['MK306674', 'MK369792', 'MK312594', 'MK382993', 'MK351616', 'MK299375', 'MK428449', 'MK323829', 'MK301892', 'MK413944', 'MK365341', 'MK409422', 'MK334737', 'MK266457', 'MK457245', 'MK451259', 'MK401938']
    baseline = []
    for i in range(len(sku_codes)):
        #Baseline between 0 and 10000
        baseline.append(random.randint(0,10000))
    for i in range(23):
        for c in range(len(sku_codes)):
            quantity = (i+1)*300 * random.uniform(0.85, 1.15) + baseline[c]
            timecode = str(1001 + i)
            newItem = SKU_History_Units(geo_code='1', sku_code=sku_codes[c], quantity=quantity, time_code=timecode).save()
    
    return JsonResponse({'status':'success, SKU history created'})

@csrf_exempt
@api_view(['POST'])
def generate_sku_future(request):
    sku_codes = ['MK306674', 'MK369792', 'MK312594', 'MK382993', 'MK351616', 'MK299375', 'MK428449', 'MK323829', 'MK301892', 'MK413944', 'MK365341', 'MK409422', 'MK334737', 'MK266457', 'MK457245', 'MK451259', 'MK401938']    
    for code in sku_codes:
        dataset = SKU_History_Units.objects.filter(sku_code=code)
        regression = run_regression(dataset, 'quantity')
        #Save to database and return JSON
        Forecast(forecasting_unit=code, intercept=regression['b'], slope=regression['w'], loss=regression['loss'], dataset_id=str(2)).save()
    return JsonResponse({'status':'success'}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def regression(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    #try:
    dataset_id = body['dataset_id']
    print("\n\nRunning Regression on Dataset: {}\n\n".format(dataset_id))
    dataset = Data.objects.filter(dataset_id=dataset_id)
    forecasting_unit = getattr(dataset[0], "forecasting_unit")

    results = {'status':'success'}
    regression = run_regression(dataset, 'values')
    results.update(regression)

    #Save to database
    forecast = Forecast(forecasting_unit=forecasting_unit, intercept=regression['b'], slope=regression['w'], loss=regression['loss'], dataset_id=dataset_id).save()
    return JsonResponse(results, status=status.HTTP_200_OK)
    #except: 
    #    return JsonResponse({'status':'regression failed'}, status=status.HTTP_400_BAD_REQUEST)

