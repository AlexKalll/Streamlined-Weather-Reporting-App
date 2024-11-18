from django.shortcuts import render, HttpResponse
#import json to load json data to python dictionary
import json
#import urllib.request to make a request to api
import urllib.request
#import os to have access to environment variables
import os
# first install python-dotenv as !pip install python-dotenv 
# then import dotenv so that we can use it
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        """use your api key in place of WEATHER_API_KEY ='your_ap_key'. you can write it in the .env file and then load it or you can put it directly in this source code as well"""

        complete_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'
        # response will contain JSON data from the API
        response = urllib.request.urlopen(complete_url).read()
        # converting json data into dictionary
        list_of_data = json.loads(response)
        #dictionary data of countries you will requests for its weather
        if list_of_data['cod'] == 200:
            data = {
                'status_code': True,
                'name': city,
                'country_code': str(list_of_data['sys']['country']),
                'weather_description': str(list_of_data['weather'][0]['description']),
                'coordinate': str(list_of_data['coord']['lon']) +'°' + ' ' + str(list_of_data['coord']['lat'])+ '°',
                'temp': str(list_of_data['main']['temp']) + 'K',
                'pressure': str(list_of_data['main']['pressure']) + "Pa",
                'humidity': str(list_of_data['main']['humidity']) +'%',
                'wind_speed': str(list_of_data['wind']['speed']) + "m/s",
            }
        else:
            data = {
                'status_code': False,
                'error': 'Error while fetching data. Please enter a correct name:)',}

    else:
        data = {}

    return render(request, 'main/index.html', data)

def picture(request):
    return render(request, 'main.pic.html')