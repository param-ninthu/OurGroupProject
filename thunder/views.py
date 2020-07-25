from django.shortcuts import render
from .models import Place
import googlemaps
from datetime import datetime
import requests


# Create your views here.

def page(request):
    return render(request, 'web.html')



#def result(request):
 #   return
 #   pl=Place()
  #  city_name = request.GET['search']
   # pl.view=False
#    gmaps = googlemaps.Client(key='AIzaSyDngj3-xgiEgzY4SquLFVTmZXu7i-S_4_s')
#    mapbox_token='pk.eyJ1IjoicGFyYW0tbmludGh1IiwiYSI6ImNrYnRxZ3U0YzAxZ2QycG53Njk1Z24zeTEifQ.1gRzSC9oNO1eCugHu6fdaA'
#    if request.method == 'GET':
#        pl.view= True
#        lat = geocode_result[0]["geometry"]["location"]["lat"]
#        lng = geocode_result[0]["geometry"]["location"]["lng"]
#        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name},&appid=eaba6a5365ac924ba37ce8b020fc2aca'
#        url_=f"https://tile.openweathermap.org/map/temp_new/9/{lat}/{lng}.png?appid=eaba6a5365ac924ba37ce8b020fc2aca"
#        res = requests.get(url)
#        data = res.json()
#        temp = float(data['main']['temp']) - 273.15
#        temperature = round(temp, 0)
#        cloud = data['weather'][0]['description']
#        icon= data['weather'][0]['icon']
#        sr= f" http://openweathermap.org/img/wn/{icon}@2x.png"
 #       Suggestions='Not bad'
 #       return render(request, 'web.html',{'Temperature': temperature, 'res': city_name, 'Status': cloud, 'Suggestions': Suggestions,'pl':pl,'mapbox_token':mapbox_token,'lat':lat,'lng':lng,'sr':sr,'url_':url_})
##,{'pl':pl}
# def result(request):
#   city_name = request.GET['search']
#  url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name},&appid=eaba6a5365ac924ba37ce8b020fc2aca'
# res = requests.get(url)
# data = res.json()
#    temp = float(data['main']['temp']) - 273.15
#   temperature =round(temp,0)
#  cloud = data['weather'][0]['description']
# return render(request, 'result.html', {'Temperature': temperature, 'res': city_name, 'Status': cloud})


def weather(request):
    pl=Place()
    city_name = request.GET.get('search',None)
    pl.view=False
    gmaps = googlemaps.Client(key='AIzaSyB5U-R8-DVyRM0WMk0KjDSo93w3SYwsY38')
    mapbox_token='pk.eyJ1IjoicGFyYW0tbmludGh1IiwiYSI6ImNrY2podWp2NzFseG4zNW54aTU2a3VlcXYifQ.5Abrf2Y2w0kjxUrELC_jPg'
    if request.method == 'GET':
        pl.view= True
        geocode_result = gmaps.geocode(f'{city_name}')
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name},&appid=eaba6a5365ac924ba37ce8b020fc2aca'
        url_=f"https://tile.openweathermap.org/map/temp_new/9/{lat}/{lng}.png?appid=eaba6a5365ac924ba37ce8b020fc2aca"
        res = requests.get(url)
        data = res.json()
        temp = float(data['main']['temp']) - 273.15
        temperature = round(temp, 0)
        cloud = data['weather'][0]['description']
        icon= data['weather'][0]['icon']
        sr= f" http://openweathermap.org/img/wn/{icon}@2x.png"
        ######### Suggestions
       # if cloud =='overcast clouds':
        #    Suggestions = "It is better to take Umbrella or cap  with you."
    return render(request , 'weather.html',{'Temperature': temperature, 'res': city_name, 'Status': cloud,'pl':pl,'mapbox_token':mapbox_token,'lat':lat,'lng':lng,'sr':sr,'url_':url_})

