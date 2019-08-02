# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#Pogoda
import pyowm
owm = pyowm.OWM('dad12bb47b731ab11ef9b3959a731c75', language='ru')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place("wroclaw")
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
print(w.get_wind())

w.get_humidity()              # 87
print(w.get_humidity())

w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.get_temperature)

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)
print(observation_list)

# And this is a usage example with a paid OWM API key:

# import pyowm

# paid_owm = pyowm.OWM(API_key='your-pro-API-key', subscription_type='pro')

# # Will it be clear tomorrow at this time in Milan (Italy) ?
# forecast = paid_owm.daily_forecast("Milan,IT")
# tomorrow = pyowm.timeutils.tomorrow()
# forecast.will_be_clear_at(tomorrow)  # The sun always shines on Italy, right? ;-)
#Hello World 123+=*
