from django.urls import path  
from .views import Weather  
urlpatterns = [  
    path('weather/', Weather, name = 'Weather')  
]  