import requests
from datetime import datetime

api_key = '6d81f202d1811922faddf53fbfef7ee8'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

with open('weather_details.txt', 'w') as f:
    f.write("\t\t\tWeather Information of {}\n\n".format(location))
    f.write("Current Date & Time of {} : {}\n".format(location, date_time))
    f.write("Current Temperature of {} : {:.2f} celcius\n".format(location,temp_city))
    f.write("Current Weather Description {} : {}\n".format(location, weather_desc))
    f.write("Current Humadity of {} : {}%\n".format(location, hmdt))
    f.write("Current Wind Speed of {} : {}kmph".format(location, wind_spd))
    