
from my_class_and_methods import WeatherData
from table class in SQLite import
#add validation for input values

#getting user input
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))
month = int(input("Enter month in numerical form: "))
day = int(input("Enter day: "))
year = int(input("Enter year: "))

#c3
#create instance of class
weather = WeatherData(latitude,longitude,month,day,year)

#call class method
weather.get_data()

