
from django.urls import path
from .views import visaInicio


urlpatterns = [
    path('vistaInicio/', visaInicio, name='vistaInicio'),
    
]


