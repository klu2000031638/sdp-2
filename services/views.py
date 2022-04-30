import json  
from django.shortcuts import render  
import urllib.request  
import json  
  
# Create your views here.  
  
def Weather(request):  
    if request.method == 'POST':  
        # Get the city name from the user api = http://api.openweathermap.org/data/2.5/weather  
        city = request.POST.get('city', 'True')  
          
        # retreive the information using api  
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=266f4d52647b4b8bf2c21a1ac29f445d').read()  
          
        # convert json data file into python dictionary  
        list_of_data = json.loads(source)  
  
        # create dictionary and convert value in string  
        context = {  
            'city': str(city.title()),  
            "country_code": str(list_of_data['sys']['country']),  
            "coordinate": str(list_of_data['coord']['lon']) + ' '  
                            + str(list_of_data['coord']['lat']),  
            "temp": str(list_of_data['main']['temp']) + 'F',  
            "pressure": str(list_of_data['main']['pressure']),  
            "humidity": str(list_of_data['main']['humidity']),  
        }  
    else:  
        context = {
            'statusCode':404,
            'body':'Your Entered Wrong details'
        }  
      
    # send dictionary to the index.html  
    return render(request, 'services/weather.html', context)  
