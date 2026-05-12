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


    def get_data(self):
        '''retrieves past 5 years of weather data from api and aggregates values'''

        temps = []
        winds = []
        precip = []

        #api call here- will use loop to append values to lists
        for yr in range(self.year-5, self.year):

            #error handling
            try:
                print(f'processing year: {yr}')
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
                #automatically checks status code and raises error if bad
                response.raise_for_status()

                #convert json response into python dictionary
                data = response.json()
                #accessing values associated w/ 'daily' key of dictionary-using indexing
                daily = data['daily']

                temps.append(daily['temperature_2m_mean'][0])
                precip.append(daily['precipitation_sum'][0])
                winds.append(daily['wind_speed_10m_max'][0])

            #catches anything wrong w/ api request
            except requests.exceptions.RequestException as e:
                print(f'something went wrong for year {yr}: {e}')

            #catches trying to access dictionary keys that don't exist
            except KeyError as e:
                print(f'Missing data for dictionary key for {yr}: {e}')

            #catches trying to access empty list
            except IndexError as e:
                print(f'Data list empty for {yr}: {e}')

        #check list length = 5
        if len(temps) != 5 or len(winds) != 5 or len(precip) !=5:
            print("Missing weather data. Cannot calculate 5 year aggregates.")
            return

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

        #test values appending to lists
       ''' print(f'temps: {temps}\n'
              f'winds: {winds}\n'
              f'precip: {precip}')

        #aggregation tests
        print(f'temp_avg5yr: {self.temp_avg5yr:.2f}')
        print(f'temp_min5yr: {self.temp_min5yr:.2f}')
        print(f'temp_max5yr: {self.temp_max5yr:.2f}')

        print(f'wind_avg5yr: {self.wind_avg5yr:.2f}\n'
        f'wind_min5yr: {self.wind_min5yr:.2f}\n'
        f'wind_max5yr: {self.wind_max5yr:.2f}')

        print(f'precip_sum5yr: {self.precip_sum5yr:.2f}')
        print(f'precip_min5yr: {self.precip_min5yr:.2f}')
        print(f'precip_max5yr: {self.precip_max5yr:.2f}')'''







