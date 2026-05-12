from my_class_and_methods import WeatherData
from class_sqlalchemy import WeatherRecord, session

#add validation for input values

#getting user input
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))
month = int(input("Enter month in numerical form: "))
day = int(input("Enter day: "))
year = int(input("Enter year: "))


#create instance of class
weather = WeatherData(latitude,longitude,month,day,year)

#call class method
weather.get_data()

#
record = WeatherRecord(
    latitude = weather.latitude,
    longitude = weather.longitude,
    month = weather.month,
    day = weather.day,
    year = weather.year,
    temp_avg5yr = weather.temp_avg5yr,
    temp_min5yr = weather.temp_min5yr,
    temp_max5yr = weather.temp_max5yr,
    wind_avg5yr = weather.wind_avg5yr,
    wind_min5yr = weather.wind_min5yr,
    wind_max5yr = weather.wind_max5yr,
    precip_sum5yr = weather.precip_sum5yr,
    precip_min5yr = weather.precip_min5yr,
    precip_max5yr = weather.precip_max5yr
)

#populates table
session.add(record)
session.commit()

