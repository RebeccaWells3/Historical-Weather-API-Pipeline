import unittest
from my_class_and_methods import WeatherData
from class_sqlalchemy import Base, WeatherRecord
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestWeatherData(unittest.TestCase):

    def test_agg_att_init(self):
        '''tests if aggregate attributes were initialized correctly. attribute type == None'''

        weather = WeatherData(47.0449, -122.9017, 5, 1, 2027)

        self.assertIsNone(weather.temp_avg5yr)
        self.assertIsNone(weather.wind_avg5yr)
        self.assertIsNone(weather.precip_sum5yr)

    def test_get_data_creates_agg_float(self):
        '''tests if get_data() creates aggregate floats'''

        weather = WeatherData(47.0449, -122.9017, 5, 1, 2027)

        weather.get_data()

        self.assertIsInstance(weather.temp_avg5yr, float)
        self.assertIsInstance(weather.wind_avg5yr, float)
        self.assertIsInstance(weather.precip_sum5yr, float)

    def test_db(self):
        '''tests if database stores and returns inserted data'''

        # temporary in-memory database
        engine = create_engine("sqlite:///:memory:")

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        #test data
        test_record = record = WeatherRecord(
            latitude = 47.0449,
            longitude = -122.9017,
            month = 5,
            day = 1,
            year = 2027,
            temp_avg5yr = 72.6,
            temp_min5yr = 29,
            temp_max5yr = 102,
            wind_avg5yr = 34,
            wind_min5yr = 5,
            wind_max5yr = 62,
            precip_sum5yr = 20,
            precip_min5yr = 0.5,
            precip_max5yr = 10
        )

        #stores row
        session.add(test_record)
        session.commit()

        #retrieves row
        stored_record = session.query(WeatherRecord).filter_by(id=test_record.id).first()

        self.assertIsNotNone(stored_record)
        self.assertEqual(stored_record.latitude, 47.0449)
        self.assertEqual(stored_record.temp_avg5yr, 72.6)

        #ends session & clears saved row
        session.close()

if __name__ == '__main__':
    unittest.main()



#query inserted row and it matches expected values

