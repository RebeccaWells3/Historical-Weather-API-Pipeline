#import specific tools instead of whole toolbox
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

#creates ORM system that tracks table definitions
Base = declarative_base()

class WeatherRecord(Base):
    '''defines blueprint for table'''

    __tablename__ = "weather_data"
    id = Column(Integer,primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)
    temp_avg5yr = Column(Float)
    temp_min5yr = Column(Float)
    temp_max5yr = Column(Float)
    wind_avg5yr = Column(Float)
    wind_min5yr = Column(Float)
    wind_max5yr = Column(Float)
    precip_sum5yr = Column(Float)
    precip_min5yr = Column(Float)
    precip_max5yr = Column(Float)

    def query_record(self):
        '''queries weather data table'''

        stored_record = session.query(WeatherRecord).filter_by(id=self.id).first()

        print("\nWeather Summary")
        print("----------------")
        print(f"Record ID: {stored_record.id}")
        print(f"Latitude: {stored_record.latitude}")
        print(f"Longitude: {stored_record.longitude}")
        print(f"Date: {stored_record.month}/{stored_record.day}/{stored_record.year}")

        print("\nTemperature")
        print(f"5-year average: {stored_record.temp_avg5yr:.2f} °F")
        print(f"5-year minimum: {stored_record.temp_min5yr:.2f} °F")
        print(f"5-year maximum: {stored_record.temp_max5yr:.2f} °F")

        print("\nWind Speed")
        print(f"5-year average: {stored_record.wind_avg5yr:.2f} mph")
        print(f"5-year minimum: {stored_record.wind_min5yr:.2f} mph")
        print(f"5-year maximum: {stored_record.wind_max5yr:.2f} mph")

        print("\nPrecipitation")
        print(f"5-year sum: {stored_record.precip_sum5yr:.2f} inches")
        print(f"5-year minimum: {stored_record.precip_min5yr:.2f} inches")
        print(f"5-year maximum: {stored_record.precip_max5yr:.2f} inches")

#creates connection between python and SQLite file. if file doesn't exist yet, creates it
engine = create_engine("sqlite:///weather.db")

#create table
Base.metadata.create_all(engine)

#set up session
Session = sessionmaker(bind=engine)

#actual session created from factory
session = Session()

