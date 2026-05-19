<h1 align="center">Historical Weather API Pipeline</h1>

Python application that retrieves five years of historical weather data from the Open-Meteo REST API, processes JSON responses into aggregate weather metrics, and stores results in a SQLite database using SQLAlchemy.

## Technologies Used 
- Python
- REST APIs
- Requests
- SQLite
- SQLAlchemy ORM
- unittest

## Data Flow
User Input → Input Validation → Open-Meteo API Request → JSON Processing → Aggregate Calculations → SQLite Storage → Record Retrieval

## Data Source
- [Open-Meteo Archive API](https://open-meteo.com/en/docs/historical-weather-api)

## Requirements
- Python 3.10+
- Requests
- SQLAlchemy

## Installation
1. Clone or download this repository.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run the Project
1. Run the main program:

```bash
python main.py
```

2. Enter the requested location and date information:
   - Latitude
   - Longitude
   - Month
   - Day
   - Year

## Example Output

Weather Summary
----------------
Record ID: 1
Latitude: 47.0449
Longitude: -122.9017
Date: 5/1/2027

Temperature
5-year average: 52.62 °F
5-year minimum: 45.30 °F
5-year maximum: 61.10 °F

Wind Speed
5-year average: 5.52 mph
5-year minimum: 3.80 mph
5-year maximum: 7.00 mph

Precipitation
5-year total: 0.55 in

## Features
- Accepts user input for latitude, longitude, month, day, and year
- Validates user input before processing
- Retrieves five years of historical weather data from the Open-Meteo API
- Calculates aggregate statistics for temperature, wind speed, and precipitation
- Stores processed weather records in a SQLite database using SQLAlchemy ORM
- Prevents incomplete data from being saved if data retrieval fails
- Automated unit testing with Python's unittest framework

## Testing
This project includes automated unit tests for core functionality, including:
- WeatherData object initialization
- Creation of aggregate weather metrics after data retrieval
- Database record storage and retrieval

Run tests with:

```bash
python -m unittest
```

## Project Structure
- [`main.py`](https://github.com/RebeccaWells3/Historical-Weather-API-Pipeline/blob/main/main.py) - Runs the application, collects user input, and saves processed records
- [`my_class_and_methods.py`](https://github.com/RebeccaWells3/Historical-Weather-API-Pipeline/blob/main/my_class_and_methods.py) - Contains the WeatherData class and API/data aggregation logic
- [`class_sqlalchemy.py`](https://github.com/RebeccaWells3/Historical-Weather-API-Pipeline/blob/main/class_sqlalchemy.py) - Defines the database model and SQLAlchemy session
- [`test.py`](https://github.com/RebeccaWells3/Historical-Weather-API-Pipeline/blob/main/test.py) - Contains unit tests for core project functionality
- [`requirements.txt`](https://github.com/RebeccaWells3/Historical-Weather-API-Pipeline/blob/main/requirements.txt) - Lists required Python packages


