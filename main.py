from my_class_and_methods import WeatherData
from class_sqlalchemy import WeatherRecord, session
from datetime import date
def main():

    #getting user input
    try:
        latitude = float(input("Enter latitude: "))
    except ValueError:
        print("latitude must be a number")
        return
    if latitude < -90 or latitude > 90:
        print("latitude must be within the range of -90 to 90")
        return

    try:
        longitude = float(input("Enter longitude: "))
    except ValueError:
        print("longitude must be a number")
        return
    if longitude <-180 or longitude >180:
        print("longitude must be within the range of -180 to 180")
        return

    try:
        month = int(input("Enter month in numerical form: "))
    except ValueError:
        print("month must be a number")
        return
    if month <1 or month >12:
        print("month must be within the range of 1 to 12")
        return

    try:
        day = int(input("Enter day: "))
    except ValueError:
        print("day must be a number")
        return
    if day <1 or day >31:
        print("day must be within the range of 1 to 31")
        return

    #weather API can't access data before 1940
    current_date = date.today()
    current_year = current_date.year
    max_year = current_year + 1
    try:
        year = int(input("Enter year: "))
    except ValueError:
        print("year must be a number")
        return
    if year <1940 or year > max_year:
        print("year must be within the range of 1940 to current year + 1")
        return


    #create instance of class
    weather = WeatherData(latitude,longitude,month,day,year)

    #call class method
    weather.get_data()

    #prevent bad data being saved
    if weather.temp_avg5yr is None:
        print("get_data function failed. try again")
        return

    #creates ORM record object representing one table row
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

    #query table
    record.query_record()

if __name__ == "__main__":
    main()

