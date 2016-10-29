import random
import info_filter

MALE_CLOTHING = {'top': {'hot': ['tank-top', 't-shirt', 'v-neck', 'polo'],
                         'avg': ['t-shirt', 'v-neck', 'polo', 'casual dress shirt'],
                         'cold': ['t-shirt', 'v-neck', 'polo', 'long-sleeve', 'casual dress shirt']},
                 'outerwear': {'hot': ['no outerwear'],
                               'avg': ['thin jacket', 'cardigan', 'thin sweater', 'thin coat', 'no outerwear'],
                               'cold': ['thick jacket', 'thick coat', 'thick sweater'],
                               'rain': ['rain coat'],
                               'snow': ['heavy snow coat'],
                               'wind': ['windbreaker']},
                 'bottom': {'hot': ['khaki shorts', 'thin athletic pants', 'basketball shorts', 'cargo shorts'],
                            'avg': ['khaki pants', 'basketball shorts', 'cargo shorts', 'athletic pants', 'jeans'],
                            'cold': ['khaki pants', 'sweatpants', 'athletic pants', 'jeans', 'cargo pants']},
                 'footwear': {'hot': ['sandals'],
                              'avg': ['sandals', 'sneakers'],
                              'cold': ['sneakers'],
                              'rain': ['boots'],
                              'snow': ['boots']}
                 }

FEMALE_CLOTHING = {'top': {'hot': ['t-shirt', 'v-neck', 'blouse', 'crop top', 'tank-top'],
                           'avg': ['t-shirt', 'v-neck', 'casual dress shirt', 'blouse'],
                           'cold': ['v-neck', 'long-sleeve', 'casual dress shirt', 'turtleneck']},
                   'outerwear': {'hot': ['cardigan', 'no outerwear'],
                                 'avg': ['cardigan', 'thin jacket', 'thin sweater', 'thin coat', 'no outerwear'],
                                 'cold': ['thick jacket', 'coat', 'thick sweater', 'hoodie', 'trenchcoat'],
                                 'rain': ['rain coat', 'poncho'],
                                 'snow': ['heavy snow coat'],
                                 'wind': ['windbreaker']},
                   'bottom': {'hot': ['short-shorts', 'mini-skirt', 'leggings'],
                              'avg': ['skirt', 'leggings', 'jeans', 'basketball shorts'],
                              'cold': ['sweatpants', 'jeans', 'athletic pants']},
                   'footwear': {'hot': ['sandals', 'flats', 'heels'],
                                'avg': ['boots', 'sneakers', 'sandals', 'flats', 'heels'],
                                'cold': ['boots', 'sneakers'],
                                'rain': ['boots'],
                                'snow': ['boots']}
                   }

class GeneratorErrorException:
    pass

class ClothingGenerator:
    def __init__(self, gender: str, current_temp: int, windspeed: int, weather_id: int):
        self.gender = gender
        self.current_temp = current_temp
        self.windspeed = windspeed
        self.weather_id = weather_id
        
        self._special_weather()
        self._general_temp()
        self._windspeed()
        
    def generate_top(self) -> str:
        if self.gender.upper() == 'MALE':
            return random.choice(MALE_CLOTHING['top'][self.temp])
        elif self.gender.upper() == 'FEMALE':
            return random.choice(FEMALE_CLOTHING['top'][self.temp])
        else:
            raise GeneratorErrorException
    
    def generate_outerwear(self) -> str:
        if self._check_special_weather():
            if (self.weather == 'thunderstorm' or self.weather == 'rain') and self.gender.upper() == 'FEMALE':
                return random.choice(FEMALE_CLOTHING['outerwear']['rain'])
            elif (self.weather == 'extreme' or self.weather == 'snow') and self.gender.upper() == 'FEMALE':
                return random.choice(FEMALE_CLOTHING['outerwear']['snow'])
            elif self.weather == 'thunderstorm' or self.weather ==  'rain' or self.weather == 'extreme':
                return random.choice(MALE_CLOTHING['outerwear']['rain'])
            elif self.weather == 'snow':
                return random.choice(MALE_CLOTHING['outerwear']['snow'])
        else:
            if self.windy:
                return random.choice(MALE_CLOTHING['outerwear']['wind'])
            elif self.gender.upper() == 'MALE':
                return random.choice(MALE_CLOTHING['outerwear'][self.temp])
            elif self.gender.upper() == 'FEMALE':
                return random.choice(FEMALE_CLOTHING['outerwear'][self.temp])
            else:
                raise GeneratorErrorException
            
    def generate_bottom(self) -> str:
        if self.gender.upper() == 'MALE':
            return random.choice(MALE_CLOTHING['bottom'][self.temp])
        elif self.gender.upper() == 'FEMALE':
            return random.choice(FEMALE_CLOTHING['bottom'][self.temp])
        else:
            raise GeneratorErrorException
    
    def generate_footwear(self) -> str:
        if self._check_special_weather():
            if (self.weather == 'thunderstorm' or self.weather == 'rain' ) and self.gender.upper() == 'FEMALE':
                return random.choice(FEMALE_CLOTHING['footwear']['rain'])
            elif self.weather == 'thunderstorm' or self.weather == 'rain':
                return random.choice(MALE_CLOTHING['footwear']['rain'])
            elif self.weather == 'snow' or self.weather == 'extreme':
                return random.choice(MALE_CLOTHING['footwear']['snow'])
            else:
                raise GeneratorErrorException
        else:
            if self.gender.upper() == 'MALE':
                return random.choice(MALE_CLOTHING['footwear'][self.temp])
            elif self.gender.upper() == 'FEMALE':
                return random.choice(FEMALE_CLOTHING['footwear'][self.temp])
            else:
                raise GeneratorErrorException
    
    def generate_misc(self) -> str:
        if self.weather == 'thunderstorm' or self.weather == 'drizzle' or self.weather == 'rain':
            return 'umbrella'
        else:
            return 'no accessories needed'
    
    def _special_weather(self):
        if self.weather_id >= 200 and self.weather_id < 300:
            self.weather = 'thunderstorm'
        elif self.weather_id >= 300 and self.weather_id < 400:
            self.weather = 'drizzle'
        elif self.weather_id >= 500 and self.weather_id < 600:
            self.weather = 'rain'
        elif self.weather_id >= 600 and self.weather_id< 700:
            self.weather = 'snow'
        elif ((self.weather_id > 701 and self.weather_id < 721)or (self.weather_id > 721 and self.weather_id < 741) or (self.weather_id>=900 and self.weather_id <907) or (self.weather_id >= 957 and self.weather_id <963)):
            self.weather = 'extreme'
        #elif self.weather_id == 701 or self.weather_id ==741 or self.weather_id == 721:
            #self.weather = 'foggy'
        else:
            self.weather = None
            
    def _windspeed(self) -> None:
        if self.windspeed >= 15:
            self.windy = True
        else:
            self.windy = False
    
    def _general_temp(self) -> None:
        if self.current_temp >= 85:
            self.temp = 'hot'
        elif self.current_temp < 85 and self.current_temp >= 70:
            self.temp = 'avg'
        else:
            self.temp = 'cold'
            
    def _check_special_weather(self) -> bool:
        if self.weather != None:
            return True
        return False
# #Test
# filter_info = info_filter.WeatherInfo('92617')
# gender = 'FEMALE'
# current_temp = filter_info.get_current_temp()
# windspeed = filter_info.get_windspeed()
# weather_id = filter_info.get_weather_id()
#  
# generator = ClothingGenerator(gender, current_temp, windspeed, weather_id)
# print('Top: ' + generator.generate_top())
# print('Outerwear: ' + generator.generate_outerwear())
# print('Bottom: ' + generator.generate_bottom())
# print('Footwear: ' + generator.generate_footwear())
# print('Misc: ' + generator.generate_misc())


    