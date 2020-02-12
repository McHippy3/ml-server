from django.urls import path, include
from sample1.views import *

urlpatterns = [
    path('', index),
    path('generate_data/', generate_data),
    path('generate_sku_history/', generate_sku_history),
    path('generate_sku_future', generate_sku_future),
    path('regression', regression),
    path('results', results),
]
