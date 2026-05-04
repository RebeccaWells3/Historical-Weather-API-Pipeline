import requests

class WeatherData:
    '''creates location and date objects'''

    def __init__(self,latitude,longitude,month,day,year):

        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year

        #five year aggregate instance variables/class attributes
        #SHOULD I PUT THEM = NONE?
        #temperature
        self.temp_avg5yr = None
        self.temp_min5yr = None
        self.temp_max5yr = None
        #windspeed
        self.wind_avg5yr = None
        self.wind_min5yr = None
        self.wind_max5yr = None

        #precipation
        self.precip_sum5yr = None
        self.precip_min5yr = None
        self.precip_max5yr = None

        #make separate class for aggregate variables?


    def get_data(self):
        '''get data using api and appends values to variable lists.
        then calculates aggregate values'''

        temps = []
        winds = []
        precip = []

        #api call here- will use loop to append values to lists

            for i in range(self.year-5,self.year):

        #aggregation time!!!
        # temperature
        self.temp_avg5yr = sum(temps) / len(temps)
        self.temp_min5yr = min(temps)
        self.temp_max5yr = max(temps)

        # windspeed
        self.wind_avg5yr = sum(winds) / len(winds)
        self.wind_min5yr = min(winds)
        self.wind_max5yr = max(winds)

        # precipitation
        self.precip_sum5yr = sum(precip)
        self.precip_min5yr = min(precip)
        self.precip_max5yr = max(precip)








