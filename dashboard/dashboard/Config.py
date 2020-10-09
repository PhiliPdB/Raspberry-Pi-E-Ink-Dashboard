from os import getenv
from dotenv import load_dotenv

load_dotenv()

# weather
icon_base_url = 'http://openweathermap.org/img/wn/'
open_weather_map_api_key = getenv("OPEN_WEATHER_MAP_API_KEY")
lat = getenv("LAT")
lon = getenv("LON")
units = getenv("UNITS")
unit_letter = 'C'

# covid
country = getenv("COUNTRY")
covid_url = 'https://disease.sh/v3/covid-19/'

# fonts
small_font_size = 14
medium_font_size = 19
large_font_size = 24

small_font_name = '/home/pi/.fonts/Rubik-Light.ttf'
medium_font_name = '/home/pi/.fonts/Rubik-Regular.ttf'
large_font_name = '/home/pi/.fonts/Rubik-Bold.ttf'
