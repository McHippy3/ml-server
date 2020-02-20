from django.urls import path, include
from time_series.views import *

urlpatterns = [
    path('load_data/', load_data),
    path('run_forecast/', run_forecast),
]
