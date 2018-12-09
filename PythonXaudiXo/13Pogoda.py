# https://openweathermap.org/appid

import pyowm

city = input("Misto:")


owm = pyowm.OWM('dad12bb47b731ab11ef9b3959a731c75',language='ru')
observation = owm.weather_at_place(city)                     # Toponym
# obs.get_reception_time(timeformat='iso')                   # ISO8601
# obs = owm.weather_at_id(2643741)                           # City ID
# obs = owm.weather_at_coords(-0.107331,51.503614)           # lat/lon

w = observation.get_weather()

temperature = w.get_temperature('celsius')['temp']

hmary = w.get_clouds()
witer = w.get_wind()['speed']
witer_deg = w.get_wind()['deg']
wologist = w.get_humidity()
time = w.get_reference_time(timeformat='iso')
tysk = w.get_pressure()['press']
tysk_more = w.get_pressure()['sea_level']

print('Danni z mista ' + city + ' : ')
print('Temperatura: ' + str(temperature) + ' °C')
print('Takoz: ' + w.get_detailed_status())
print('Hmarnist : ' + str(hmary) + ' %' )
print('Witer: ' + str(witer) + ' m/s /'  + ' Stupin DEG: ' + str(witer_deg))
print('Wologist : ' + str(wologist) + ' %')
print('danni na : ' + str(time) )
print('Atmosfernyj tysk: ' + str(tysk) + ' Nad rivnem morja: ' + str(tysk_more))
print('Chas shodu soncja: ' + w.get_sunrise_time('iso'))
print('Chas zahodu soncja: ' + w.get_sunset_time('iso'))
print('Kod OWM pogody: ' + str(w.get_weather_code() ))
# print(sh.get_station_ID())
# import pyowm

# owm = pyowm.OWM('your-API-key')  # You MUST provide a valid API key

# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_place('London,GB')
# w = observation.get_weather()
# print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>

# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)
