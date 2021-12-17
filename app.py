import requests
import time

from pymongo import MongoClient
from flask import Flask,render_template,jsonify,request


app = Flask(__name__)


client = MongoClient("mongodb+srv://Dexter:passwordABC@cluster0.o3r8x.mongodb.net/WeatherDB?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.get_database('WeatherDB')




r1=requests.get("https://api.openweathermap.org/data/2.5/weather?q=Mexico%20City&APPID=2ee475268973f586496f80acda284557")
r2=requests.get("https://api.openweathermap.org/data/2.5/weather?q=Pasto&APPID=2ee475268973f586496f80acda284557")
r3=requests.get("https://api.openweathermap.org/data/2.5/weather?q=Manchester&APPID=2ee475268973f586496f80acda284557")
r4=requests.get("https://api.openweathermap.org/data/2.5/weather?q=Sapporo&APPID=2ee475268973f586496f80acda284557")

if r1.status_code == 200:
   mexicocity = r1.json()
   print(mexicocity)
   db.MexicoCity.insert_one(mexicocity)
else:
   exit()
   
if r2.status_code == 200:
   pasto = r2.json()
   print(pasto)
   db.Pasto.insert_one(pasto)
else:
   exit()  
      
if r3.status_code == 200:
   manchester = r3.json()
   print(manchester)
   db.Manchester.insert_one(manchester)
else:
   exit() 
   
   
if r4.status_code == 200:
   sapporo = r4.json()
   print(sapporo)
   db.Sapporo.insert_one(sapporo)
else:
   exit()        
        
        
@app.route('/')
def home():
    mexicocity = r1.json()
    pasto      = r2.json()
    manchester = r3.json()
    sapporo    = r4.json()
    return render_template('home.html', **locals())     



# %% Mexico City
@app.route('/mexicocity')
def mexicocity():
    mexicocity = r1.json()
    cityName = mexicocity['name']
    country= mexicocity['sys']['country']
    localtime = mexicocity['timezone']    
    cityLongitud = mexicocity['coord']['lon']
    cityLatitud = mexicocity['coord']['lat']
    temp_K  = mexicocity['main']['temp'] -273
    humidity = mexicocity['main']['humidity']
    pressure = 0.0295*mexicocity['main']['pressure']    
    wind_speed = mexicocity['wind']['speed']

    return render_template('MexicoCity.html', **locals())   


# %% Pasto
@app.route('/pasto')
def pasto():
    pasto = r2.json()
    cityName = pasto['name']
    country= pasto['sys']['country']
    localtime = pasto['timezone']    
    cityLongitud = pasto['coord']['lon']
    cityLatitud = pasto['coord']['lat']
    temp_K      = pasto['main']['temp'] -273
    humidity = pasto['main']['humidity']
    pressure = 0.0295*pasto['main']['pressure']    
    wind_speed = pasto['wind']['speed']

    return render_template('Pasto.html', **locals())   




# %% Manchester
@app.route('/manchester')
def manchester():
    manchester = r3.json()
    cityName = manchester['name']
    country= manchester['sys']['country']
    localtime = manchester['timezone']    
    cityLongitud = manchester['coord']['lon']
    cityLatitud = manchester['coord']['lat']
    temp_K  = manchester['main']['temp'] -273
    humidity = manchester['main']['humidity']
    pressure = 0.0295*manchester['main']['pressure']    
    wind_speed = manchester['wind']['speed']

    return render_template('Manchester.html', **locals())  



# %% Sapporo
@app.route('/sapporo')
def sapporo():
    sapporo = r4.json()
    cityName = sapporo['name']
    country= sapporo['sys']['country']
    localtime = sapporo['timezone']    
    cityLongitud = sapporo['coord']['lon']
    cityLatitud = sapporo['coord']['lat']
    temp_K  = sapporo['main']['temp'] -273
    humidity = sapporo['main']['humidity']
    pressure = 0.0295*sapporo['main']['pressure']    
    wind_speed = sapporo['wind']['speed']

    return render_template('Sapporo.html', **locals())      






if __name__ == "__main__":
    app.run()