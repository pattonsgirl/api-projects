# Forecaster using Weather API

## Environment setup
- python3

## Running code

- This folder contains two `.py` files.  
    - [parse-forecast-use-api.py](parse-forecast-use-api.py) is a student demo that both:
        - fetches content from the weather API using a query
        - takes the json data returned from the query and parses it
    - [parse-forecast.py](parse-forecast.py) 
        - assumes you made the weather API query, and stored the returned JSON data in a file
        - parses the JSON file only.  
    - [forecast.json](forecase.json) has a sample of JSON returned from a valid weather API query
- Run either with `python3 *filename*.py`

## Basic functionality

- Weather API query URL: `https://api.weather.gov/points/39.758949,-84.191605`
    - where `39.758949,-84.191605` are the lat/lon coordinates for Dayton, OH
- A valid query returns JSON formatted weather data.  
- Python has JSON parsing libraries, now to seek values stored in properties

## Sources

- CS 2900 - Data Science with Python - Summer 2021?