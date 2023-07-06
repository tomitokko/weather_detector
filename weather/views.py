from django.shortcuts import render
import json
import requests
from django.http import Http404

# Create your views here.
def index(request):
    try:
        if request.method == "POST":
            city = request.POST['city']
            res = requests.get('http://api.weatherapi.com/v1/current.json?key={API Key} &q='+city+'&aqi=no')

            json_data = json.loads(res.text)

            data = {
                "country_code":str(json_data['location']['country']),
                "time_zone":str(json_data['location']['tz_id']),
                    "coordinate": str(json_data['location']['lon']) + ' ' + str(json_data['location']['lat']),
                "temp":str(json_data['current']['temp_c'])+'c',
                "pressure":str(json_data['current']['pressure_mb']),
                "humidity":str(json_data['current']['humidity']),
            }

        else:
            city = ""
            data = ""
            json_data = {}

    except:
        #  raise Http404("city does not exist")
        data = "city does not exist"



    return render(request,'weather/index.html',{'city':city , 'data':data})
