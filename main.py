from my_class&methods.py
#create custom error handling for input?

#getting user input
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))
month = int(input("Enter month in numerical form: "))
day = int(input("Enter day: "))
year = int(input("Enter year: "))

#set class to variable
weather = WeatherData(latitude,longitude,month,day,year)

weather.get_data()
