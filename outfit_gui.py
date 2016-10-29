import tkinter
import info_filter
import clothing_generator
import time

DEFAULT_FONT = ('Century Gothic', 18)

class UserInputs:
    def __init__(self):
        self._window = tkinter.Tk()
        self._window.resizable(width = False, height = False)
        self._window.title('BaeCast')
        self._window.configure(background = 'lightblue')
        
        self._options_title()
        
        self._create_ok_button()
        self._ok_clicked = False

        self._name_var = tkinter.StringVar()
        self._input_name()
                
        self._gender_var = tkinter.StringVar()
        self._gender_options()
        
        self._city_var = tkinter.StringVar()
        self._input_city()
        
        self._zipcode_var = tkinter.StringVar()
        self._input_zipcode()
        
        self._name = ''
        self._gender = ''
        self._city = ''
        self._zipcode = ''
        
        
    def show(self):
        self._window.wait_window()
        
        
    def get_ok_clicked(self):
        return self._ok_clicked
    
    
    def get_name(self):
        return self._name
    
    
    def get_gender(self):
        return self._gender
    
    
    def get_city(self):
        return self._city
    
    
    def get_zipcode(self):
        return self._zipcode
        
        
    def _options_title(self):
        options_label = tkinter.Label(master = self._window, text = 'BaeCast: The Love Forecast',
                                      font = ('Century Gothic', 25))
        options_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 5,
                           sticky = tkinter.E + tkinter.W + tkinter.N + tkinter.S)
        options_label.configure(background = 'lightblue')
        
        
    def _create_ok_button(self):
        _ok_button = tkinter.Button(
            self._window, text = 'OK', font = ('Century Gothic', 20),
            command = self._on_ok_button)
        _ok_button.grid(
            row = 6, column = 1, padx = 10, pady = 5, sticky = tkinter.E + tkinter.N)
        _ok_button.configure(background = 'lightblue')
        
        
    def _on_ok_button(self):
        self._name = self._name_var.get()
        self._gender = self._gender_var.get()
        self._city = self._city_var.get()
        self._zipcode = self._zipcode_var.get()
        
        if len(self._zipcode) != 5:
            reminder = tkinter.Label(self._window,text = 'Please complete the form.\nZip code must be 5 digits.',
                                font = ('Century Gothic', 12),fg = 'red')
            reminder.grid(row = 6, column = 0, padx = 10, sticky = tkinter.E)
            reminder.configure(background = 'lightblue')
        else:
            
            self._ok_clicked = True
            self._window.destroy()
        
    
    def _input_name(self):
        name_label = tkinter.Label(master = self._window, text = 'Name: ',
                                   font = DEFAULT_FONT)
        name_label.grid(row = 1, column = 0, padx = 10, pady = 5,
                          sticky = tkinter.W + tkinter.N)
        
        name_entry = tkinter.Entry(master = self._window, textvariable = self._name_var, font = DEFAULT_FONT)
        name_entry.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 5, 
                        sticky = tkinter.E + tkinter.N)
        name_label.configure(background = 'lightblue')
        
    def _gender_options(self):
        gender_label = tkinter.Label(master = self._window, text = 'Gender: ', 
                                     font = DEFAULT_FONT)
        gender_label.grid(row = 2, column = 0, padx = 10, pady = 5,
                          sticky = tkinter.W + tkinter.N)
        gender_label.configure(background = 'lightblue')
        
        _first_turn_choice1 = tkinter.Radiobutton(
            self._window, font = DEFAULT_FONT,
            text = ('Male'), variable = self._gender_var, value = 'male' )
        _first_turn_choice2 = tkinter.Radiobutton(
            self._window, font = DEFAULT_FONT,
            text = ('Female'), variable = self._gender_var, value = 'female')

        _first_turn_choice1.grid(
            row = 2, column = 1, padx = 10, pady = 5, sticky = tkinter.E + tkinter.N)
        _first_turn_choice2.grid(
            row = 2, column = 2, padx = 10, pady = 5, sticky = tkinter.E + tkinter.N)

        self._gender_var.set('male')
        
        _first_turn_choice1.configure(background = 'lightblue')
        _first_turn_choice2.configure(background = 'lightblue')
        
        
    def _input_city(self):
        city_label = tkinter.Label(master = self._window, text = 'City: ',
                                   font = DEFAULT_FONT)
        city_label.grid(row = 3, column = 0, padx = 10, pady = 5,
                          sticky = tkinter.W + tkinter.N)
        
        city_entry = tkinter.Entry(master = self._window, textvariable = self._city_var, font = DEFAULT_FONT)
        city_entry.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 5, 
                        sticky = tkinter.E + tkinter.N)
        city_label.configure(background = 'lightblue')
        
        
    def _input_zipcode(self):
        zipcode_label = tkinter.Label(master = self._window, text = 'Zipcode: ',
                                   font = DEFAULT_FONT)
        zipcode_label.grid(row = 4, column = 0, padx = 10, pady = 5,
                          sticky = tkinter.W + tkinter.N)
        
        zipcode_entry = tkinter.Entry(master = self._window, textvariable = self._zipcode_var, font = DEFAULT_FONT)
        zipcode_entry.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 5, 
                        sticky = tkinter.E + tkinter.N)
        zipcode_label.configure(background = 'lightblue')
        
        

    
class OutfitProgram:
    def __init__(self, name, gender, zipcode):
        self._window = tkinter.Tk()
        self._window.resizable(width = False, height = False)
        self._window.title('BaeCast')
        self._window.configure(background = 'lightblue')
        
        
        
        filter_info = info_filter.WeatherInfo(zipcode)
        current_temp = filter_info.get_current_temp()
        windspeed = filter_info.get_windspeed()
        self.weather_id = filter_info.get_weather_id()
        self._weather_conditions()
        
        
        self._name = name
        self._title()
        
        self._location = filter_info.get_city_name()
        self._location_label()
        
        self._date = time.strftime('%B %d, %Y')
        #self._date = current_day.isoformat()
        self._date_label()
        
        self._image_name = filter_info.get_picture_info()
        self._weather_image()
        
        self._weather_description = filter_info.get_weather_desc()
        self._weather_description_label()
        
        self._temp = str(filter_info.get_current_temp()) + '\xb0' +'F'
        self._temp_label()
        
        min,max = filter_info.get_max_min()
        
        self._min_temp = str(min) + '\xb0' +'F'
        self._min_temp_label()
        
        self._max_temp = str(max) + '\xb0' +'F'
        self._max_temp_label()
        
        #self._precipitation = '5%'
        #self._precipitation_label()
        
        self._humidity = str(filter_info.get_humidity()) + '%'
        self._humidity_label()
        
        self._wind = str(filter_info.get_windspeed()) + ' mph'
        self._wind_label()
        
        self._sunrise_image()
        self._sunset_image()
        
        sunrise,sunset = filter_info.get_sunrise_sunset_time()
        
        
        self._sunrise_time = sunrise + 'AM PST\n(+1:00/2:00/3:00\nFor MST/CST/EST)'
        self._sunrise_label()
        
        self._sunset_time = sunset + 'PM PST\n(+1:00/2:00/3:00\nFor MST/CST/EST)'
        self._sunset_label()
        
        self._gender = gender
        self._gender_image()
        
        self._clothing_description()
        
        self._generator = clothing_generator.ClothingGenerator(gender, current_temp, windspeed, self.weather_id)
        self._outfit_list = ['...a {},'.format(self._generator.generate_top()),
                             'a {},'.format(self._generator.generate_outerwear()),
                             'some sexy {},'.format(self._generator.generate_bottom()),
                             'and a pair of comfortable {}'.format(self._generator.generate_footwear())]
        self._outfit_label()
        
        self._window.update()
        h = self._window.winfo_height()
        w = self._window.winfo_width()
         
        ws = self._window.winfo_screenwidth() # width of the screen
        hs = self._window.winfo_screenheight()
         
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) - 40
         
        self._window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        
        
    def start(self):
        
        self._window.mainloop()
    
        
        
    def _title(self):
        title = tkinter.Label(master = self._window, text = 'Hi ' + self._name + ',\nThis is what you should wear today!',
                              font = ('Century Gothic', 25))
        title.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 0,
                        sticky = tkinter.W + tkinter.E)
        title.configure(background = 'lightblue')
        
        
    def _location_label(self):
        location = tkinter.Label(master = self._window, text = self._location,
                                 font = ('Century Gothic', 15,'bold'), width = 25)
        location.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 0, 
                      sticky = tkinter.W + tkinter.E + tkinter.N)
        location.configure(background = 'lightblue')
        
    
    def _date_label(self):
        date = tkinter.Label(master = self._window, text = self._date,
                             font = ('Century Gothic', 13))
        date.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 0,
                  sticky = tkinter.W + tkinter.E + tkinter.N)
        date.configure(background = 'lightblue')
        
        
    def _weather_image(self):
        image_dict = {'sunny': 'sunny.gif','rainy':'rain.gif','snowy':'snow.gif',
                      'cloudy':'clouds.gif','night':'moon.gif','storm':'thunderstorm.gif',
                      'extreme':'extreme.gif','partly cloudy': 'clouds.gif','hazy':'hazy.gif','foggy':'fog.gif'}
        
        img = tkinter.PhotoImage(file=image_dict[self._image_name])
        image_label = tkinter.Label(self._window, image=img, width = 150, height = 150)
        image_label.image = img
        image_label.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 0,
                   sticky = tkinter.W + tkinter.E + tkinter.N)
        image_label.configure(background = 'lightblue')


    def _weather_description_label(self):
        description = tkinter.Label(master = self._window, text = self._weather_description,
                                    font = ('Century Gothic', 17))
        description.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 0,
                         sticky = tkinter.W + tkinter.E + tkinter.N)
        description.configure(background = 'lightblue')
        
        
    def _temp_label(self):
        temp = tkinter.Label(master = self._window, text = self._temp,
                             font = ('Times New Roman', 60))
        temp.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 0, 
                  sticky = tkinter.W + tkinter.E + tkinter.N)
        temp.configure(background = 'lightblue')
        
        
    def _min_temp_label(self):
        min_temp = tkinter.Label(master = self._window, text = 'Min: {}'.format(self._min_temp),
                                     font = ('Century Gothic', 14,'italic', 'bold'))
        min_temp.grid(row = 6, column = 0, padx = 10, pady = 0, 
                  sticky = tkinter.W + tkinter.E + tkinter.N)
        min_temp.configure(background = 'lightblue')
        
        
    def _max_temp_label(self):
        max_temp = tkinter.Label(master = self._window, text = 'Max: {}'.format(self._max_temp),
                                     font = ('Century Gothic', 14,'italic', 'bold'))
        max_temp.grid(row = 6, column = 1, padx = 10, pady = 0, 
                  sticky = tkinter.W + tkinter.E + tkinter.N)
        max_temp.configure(background = 'lightblue')
       
        
    def _precipitation_label(self):
        precipitation = tkinter.Label(master = self._window, text = ('Precipitation:', self._precipitation),
                             font = ('Century Gothic', 15))
        precipitation.grid(row = 7, column = 0, columnspan = 2, padx = 10, pady = 0, 
                  sticky = tkinter.W + tkinter.E + tkinter.N)
        precipitation.configure(background = 'lightblue')
        
        
    def _humidity_label(self):
        humidity = tkinter.Label(master = self._window, text = ('Humidity:', self._humidity),
                             font = ('Century Gothic', 15))
        humidity.grid(row = 8, column = 0, columnspan = 2, padx = 10, pady = 0, 
                  sticky = tkinter.W + tkinter.E + tkinter.N)
        humidity.configure(background = 'lightblue')
          
        
    def _wind_label(self):
        wind = tkinter.Label(master = self._window, text = ('Wind: '+ self._wind),
                             font = ('Century Gothic', 15))
        wind.grid(row = 9, column = 0, columnspan = 2, padx = 10, pady = 0, 
                  sticky = tkinter.W + tkinter.E + tkinter.N)
        wind.configure(background = 'lightblue')
        
    
    def _sunrise_image(self):
        img = tkinter.PhotoImage(file='sunrise.gif')
        image_label = tkinter.Label(self._window, image=img, width = 50, height = 50)
        image_label.image = img
        image_label.grid(row = 10, column = 0, padx = 10, pady = 0,
                   sticky = tkinter.W + tkinter.E + tkinter.N)
        image_label.configure(background = 'lightblue')
        
        
    def _sunset_image(self):
        img = tkinter.PhotoImage(file='sunset.gif')
        image_label = tkinter.Label(self._window, image=img, width = 50, height = 50)
        image_label.image = img
        image_label.grid(row = 10, column = 1, padx = 10, pady = 0,
                   sticky = tkinter.W + tkinter.E + tkinter.N)
        image_label.configure(background = 'lightblue')
        
        
    def _sunrise_label(self):
        sunrise = tkinter.Label(master = self._window, text = self._sunrise_time,
                             font = ('Century Gothic', 10))
        sunrise.grid(row = 11, column = 0, padx = 10, pady = 0, 
                  sticky = tkinter.W + tkinter.E + tkinter.N)
        sunrise.configure(background = 'lightblue')
        
        
    def _sunset_label(self):
        sunset = tkinter.Label(master = self._window, text = self._sunset_time,
                             font = ('Century Gothic', 10))
        sunset.grid(row = 11, column = 1, padx = 10, pady = 0, 
                  sticky = tkinter.W + tkinter.E + tkinter.N)
        sunset.configure(background = 'lightblue')
        
        
    def _gender_image(self):
        gender_dict = {'female': 'female.gif', 'male':'male.gif'}
        img = tkinter.PhotoImage(file=gender_dict[self._gender])
        image_label = tkinter.Label(self._window, image=img, width = 50, height = 50)
        image_label.image = img
        image_label.grid(row = 1, column = 2, rowspan = 4, columnspan = 2, padx = 10, pady = 0,
                   sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S)
        image_label.configure(background = 'lightblue')
        
        
    def _clothing_description(self):
        description = tkinter.Label(master = self._window, 
                                    text = (self._weather_description + ',\nyou should wear...'),
                             width = 25, font = ('Century Gothic', 20))
        description.grid(row = 5, column = 2, padx = 10, pady = 0, 
                  sticky = tkinter.W + tkinter.E + tkinter.N)
        description.configure(background = 'lightblue')
        
        
    def _outfit_label(self):
        outfit_str = ''
        for outfit in self._outfit_list:
            outfit_str += (outfit + '\n')
        if self.weather == 'a thunderstorm' or self.weather == 'rain' or self.weather == 'drizzling rain':
            outfit_str += '\nThere is {} outside,\nyou should also bring an\n{}\n\nDon\'t catch a cold!\n'.format(self.weather, self._generator.generate_misc())
        else:
            outfit_str += '\nThere is no need to\nbring anything else!\n\nHave an amazing day!\nGood luck finding your bae! ;)\n'
        outfit_label = tkinter.Label(master = self._window, text = outfit_str[:-1],
                                     font = ('Century Gothic', 13))
        outfit_label.grid(row = 6, column = 2, rowspan = 6, padx = 10, pady = 5,
                          sticky = tkinter.W + tkinter.E + tkinter.N)
        outfit_label.configure(background = 'lightblue')
        
    def _weather_conditions(self):
        if self.weather_id >= 200 and self.weather_id < 300:
            self.weather = 'a thunderstorm'
        elif self.weather_id >= 300 and self.weather_id < 400:
            self.weather = 'drizzling rain'
        elif self.weather_id >= 500 and self.weather_id < 600:
            self.weather = 'rain'
        elif self.weather_id >= 600 and self.weather_id< 700:
            self.weather = 'snow'
        elif (self.weather_id >= 700 and self.weather_id < 800) or (self.weather_id >= 900 and self.weather_id < 906) or (self.weather_id >= 957 and self.weather_id < 962):
            self.weather = 'extreme'
        else:
            self.weather = None
        
        
        
if __name__ == '__main__':
    inputs = UserInputs()
    inputs.show()
    
    if inputs.get_ok_clicked():
        name = inputs.get_name()
        gender = inputs.get_gender()
        zipcode = inputs.get_zipcode()
        
        OutfitProgram(name, gender, zipcode).start()
# Fonts - Hannotate, Comic Sans MS, Bradley Hand Bold, SignPainter, Xingkai, YuppySC-Regular




