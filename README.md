<h1 align="center">Historical Weather API Pipeline</h1>

Python application that takes user input, retrieves five years of historical weather data from a REST API, calculates aggregate weather statistics, and stores the results in a SQLite database.

## Technologies Used 
- Python
- Requests
- SQLAlchemy
- SQLite
- REST APIs
- Object-Oriented Programming
- Exception handling
- Unit testing (unittest)

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

## Features
- Accepts user input for latitude, longitude, month, day, and year
- Validates user input before processing
- Retrieves five years of historical weather data from the Open-Meteo API
- Calculates aggregate statistics for temperature, wind speed, and precipitation
- Stores processed weather records in a SQLite database using SQLAlchemy ORM
- Prevents incomplete data from being saved if data retrieval fails
- Automated unit testing with Python's unittest framework

## Project Structure
- [`main.py`](https://gitlab.com/wgu-gitlab-environment/student-repos/rwel113/d493-scripting-and-programming-applications/-/blob/main/main.py?ref_type=heads) - Runs the application, collects user input, and saves processed records
- [`my_class_and_methods.py`](https://gitlab.com/wgu-gitlab-environment/student-repos/rwel113/d493-scripting-and-programming-applications/-/blob/main/my_class_and_methods.py?ref_type=heads) - Contains the WeatherData class and API/data aggregation logic
- [`class_sqlalchemy.py`](https://gitlab.com/wgu-gitlab-environment/student-repos/rwel113/d493-scripting-and-programming-applications/-/blob/main/class_sqlalchemy.py?ref_type=heads) - Defines the database model and SQLAlchemy session
- [`test.py`](https://gitlab.com/wgu-gitlab-environment/student-repos/rwel113/d493-scripting-and-programming-applications/-/blob/main/test.py?ref_type=heads) - Contains unit tests for core project functionality
- [`requirements.txt`](https://gitlab.com/wgu-gitlab-environment/student-repos/rwel113/d493-scripting-and-programming-applications/-/blob/main/requirements.txt?ref_type=heads) - Lists required Python packages

## Testing
This project includes unit tests for core functionality, including aggregate attribute initialization, data retrieval, and database record storage/retrieval.

Run tests with:

```bash
python -m unittest
```
