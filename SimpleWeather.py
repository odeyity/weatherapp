
import cgitb
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps



owm = OWM('ENTER API TOKEN')
mgr = owm.weather_manager()

City = input("Enter city name.. ")

observation = mgr.weather_at_place(City)
w = observation.weather

print("Weather:",w.detailed_status)             
print("Humidity:",w.humidity,"%")             
print("Temp.",w.temperature("celsius")['temp'],"°C")           

print("Press any key to exit.. ")
input()
