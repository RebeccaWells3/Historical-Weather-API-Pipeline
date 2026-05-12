#import specific tools instead of whole toolbox
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker
#c4
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

#create connection between python and SQLite file. if file doesn't exist yet, creates it
engine = create_engine("sqlite:///weather.db")