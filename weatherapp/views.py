import time
from django.shortcuts import redirect, render
from datetime import date,datetime
import requests
from .models import City
from django.contrib import messages
# from .models import city
# Create your views here.
def index(request):
    url  = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=b7aa5c17f841e6c64c4c804ffeadbe57'
    cities = City.objects.all()
    # print(cities)
    # for city in cities:
    #         print(city.name)

    city_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        kelvin=273
        today = date.today()
        # print(r.text)
        timezone = r['timezone']
        sunrisetimestamp=r['sys']['sunrise']+timezone
        sunsettimestamp=r['sys']['sunset']+timezone
        
        
        sunrise = datetime.fromtimestamp(sunrisetimestamp)
        sunset = datetime.fromtimestamp(sunsettimestamp)
        city_weather = {
            'city':city.name,
            'temprature':"{:.1f}".format(r['main']['temp']-kelvin),
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
            'temp_min': "{:.1f}".format(r['main']['temp_min']-kelvin),
            'temp_max': "{:.1f}".format(r['main']['temp_max']-kelvin),
            'step': r['main']['temp_max']-r['main']['temp_max'],
            'date':today,
            'humidity':r['main']['humidity'],
            'wind_speed':r['wind']['speed'],
            'sunrise':sunrise,
            'sunset':sunset,
            
            
        }
        city_data.append(city_weather)
    
    context = {
        'city_data':city_data,

    }

    if request.method=='GET':
        return render(request,"index.html",context)     
    
    if request.method=='POST':
        city_name = request.POST['city_name']
        r = requests.get(url.format(city_name)).json()
        city_exists = 0
        for city in cities:
            if city_name.upper() == city.name.upper():
                city_exists+=1
        if city_exists==0:
            if r['cod'] == 200:
                City.objects.create(name = city_name)
                messages.success(request,"City added") 
            else:
                messages.warning(request,"City does not exist!")       
        else:
            messages.info(request,"City already exists.")
        
            
            
                          
    # return render(request,'index.html',context)        
    return redirect('index')
        

    

def delete_city(request,city_name):
    del_city = City.objects.get(name=city_name)
    del_city.delete()
    messages.success(request,"City Removed")
    return redirect('index')
