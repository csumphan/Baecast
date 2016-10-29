#El Ninun
import api_connect
from datetime import datetime

####################################################################################################

class WeatherInfo:
    def __init__(self,zip_code: str):
        '''Takes in a zip code'''
        self.json = api_connect.get_response(api_connect.build_url_from_zip(zip_code))
        
        
    def get_weather_id(self) -> int:
        '''Returns weather id'''
        
        weather_id = int(self.json['weather'][0]['id'])
        return weather_id
        
    def get_max_min(self) -> 'tuple of int':
        '''Return the minimum and max temperature of the day'''
         
        min = float(self.json['main']['temp_min'])
        max = float(self.json['main']['temp_max'])
        
        to_fahrenheit = lambda kelvin: (kelvin*(9/5))-459.67
        min = int(to_fahrenheit(min))
        max = int(to_fahrenheit(max))
        
        return min,max
        
    def get_windspeed(self) -> float:
        '''Return the float of windspeed from json file'''
        
        wind_speed = float(self.json['wind']['speed'])
        
        to_miles_per_hour = lambda speed: (speed*2.236936)
        wind_speed = round(to_miles_per_hour(wind_speed),1)
        
        return wind_speed
    
    def get_weather_desc(self) -> str:
        '''Return the string defining the weather description'''
        
        description = self.json['weather'][0]['description']
        
        return description.title()
    
    def get_sunrise_sunset_time(self) -> 'tuple of str':
        '''Return the tuple defining time when the sunrise and sunset 
           in the form (sunrise,sunset).'''
        
        sunrise = self.json['sys']['sunrise']
        sunset = self.json['sys']['sunset']
        
        sunrise_time = datetime.fromtimestamp(int(sunrise)).strftime('%H:%M')
        sunset_time = datetime.fromtimestamp(int(sunset)).strftime('%H:%M')
        
        return convert_time(sunrise_time),convert_time(sunset_time)

    def get_humidity(self) -> int:
        '''Return the int for percent humidity'''
        
        humidity = self.json['main']['humidity']
        
        return humidity   
        
    def get_city_name(self) -> str:
        '''Return the city name in a string form'''
        
        city_name = self.json['name']
        return city_name
    
    def get_current_temp(self) -> int:
        '''Return the current temperature in an int form'''
        
        current_temp = self.json['main']['temp']
        
        to_fahrenheit = lambda kelvin: (kelvin*(9/5))-459.67
        current_temp = int(to_fahrenheit(current_temp))
        
        return current_temp
                
    def get_picture_info(self):
        
        sunrise = self.json['sys']['sunrise']
        sunset = self.json['sys']['sunset']
        current_time = self.json['dt']
        
        sunrise_time = datetime.fromtimestamp(int(sunrise)).strftime('%H:%M')
        sunset_time = datetime.fromtimestamp(int(sunset)).strftime('%H:%M')
        current_time = datetime.fromtimestamp(int(current_time)).strftime('%H:%M')
        rise_hour = sunrise_time.split(':')[0]
        fall_hour = sunset_time.split(':')[0]
        
        current_hour = current_time.split(':')[0]
        
        if int(current_hour) <= int(rise_hour) and int(current_hour) >= int(fall_hour):
            return 'night'
        
        id = self.get_weather_id()
        
        if id >= 200 and id < 300:
            return 'storm'
        
        elif (id >= 300 and id <400) or (id >= 500 and id < 600):
            return 'rainy'
        
        elif id >= 600 and id < 700:
            return 'snowy'
        elif ((id > 701 and id < 721)or (id > 721 and id < 741) or (id>=900 and id <907) or (id >= 957 and id <963)):
            return 'extreme'
        
        elif(id == 701 or id ==741):
            return 'foggy'
        
        elif (id == 721):
            return 'hazy'
        
        elif id >= 803 and id < 805:
            return 'cloudy'
        elif id >= 801 and id <803:
            return 'partly cloudy'
        
        elif id == 800:
            return 'sunny'
        
        

########################################################

def convert_time(time:str):
    hour_min = time.split(':')
    hour = hour_min[0]
    
    if int(hour) > 12:
        new_hour = int(hour) - 12
        
        return str(new_hour) + ':' + hour_min[1]
    
    return time[1:]

#################################################################
#Test
#print(WeatherInfo('91345').get_windspeed())