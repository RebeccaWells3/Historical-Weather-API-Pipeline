
class WeatherData:
    '''creates location and date objects'''

    def __init__(self,latitude,longitude,month,day,year,temp_avg5yr,temp_min5yr,temp_max5yr,
                 wind_avg5yr,wind_min5yr,wind_max5yr,precip_sum5yr,precip_min5yr,precip_max5yr):

        self.latitude = 47.0449
        self.longitude = -122.9017
        self.month = 5
        self.day = 29
        self.year = 2026

        #five year aggregate instance variables/class attributes
        #SHOULD I PUT THEM = NONE?
        #temperature
        self.temp_avg5yr = temp_avg5yr
        self.temp_min5yr = temp_min5yr
        self.temp_max5yr = temp_max5yr

        #windspeed
        self.wind_avg5yr = wind_avg5yr
        self.wind_min5yr = wind_min5yr
        self.wind_max5yr = wind_max5yr

        #precipation
        self.precip_sum5yr = precip_sum5yr
        self.precip_min5yr = precip_min5yr
        self.precip_max5yr = precip_max5yr

        #make separate class for aggregate variables?


    def get_data(self):
        '''get data using api and appends values to variable lists.
        then calculates aggreate values'''

        self.temps = []
        self.winds = []
        self.precip = []

        #api call here- will use loop to append values to lists

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

    '''def aggregate_stats(self,temps,winds,precip):
        #c2
        #calculates aggregate values

        #temperature
        self.temp_avg5yr = sum(temps)/len(temps)
        self.temp_min5yr = min(temps)
        self.temp_max5yr = max(temps)

        #windspeed
        self.wind_avg5yr = sum(winds)/len(winds)
        self.wind_min5yr = min(winds)
        self.wind_max5yr = max(winds)

        #precipitation
        self.precip_sum5yr = sum(precip)
        self.precip_min5yr = min(precip)
        self.precip_max5yr = max(precip)'''






