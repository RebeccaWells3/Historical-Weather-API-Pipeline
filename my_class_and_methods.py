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

        for yr in range(self.year-5, self.year):
            date = f"{yr:04d}-{self.month:02d}-{self.day:02d}"
            url = "https://archive-api.open-meteo.com/v1/archive"

            query_params = {
                "latitude": self.latitude,
                'longitude': self.longitude,
                "start_date": date,
                "end_date": date,
                "daily": "temperature_2m_mean,precipitation_sum,wind_speed_10m_max",
                "temperature_unit": "fahrenheit",
                "wind_speed_unit": "mph",
                "precipitation_unit": "inch"
            }

            response = requests.get(url,params=query_params)

            #response.json()




        ''''#aggregation time!!!
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
        self.precip_max5yr = max(precip'''








