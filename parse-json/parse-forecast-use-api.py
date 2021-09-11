#Most fun by R.M:
## Install requests, python-dateutil, pytz, jsonlib-python3

# Part 3
import json
import requests
import dateutil.parser
from pytz import timezone

# Send request for current information to NWS
locationInfo = requests.get('https://api.weather.gov/points/39.758949,-84.191605').json()
localForecastData = requests.get(locationInfo['properties']['forecast']).json()

# Get the update-time in the response. Convert it to local timezone and format for output.
eastern = timezone('US/Eastern')
parsedTime = dateutil.parser.parse(localForecastData['properties']['updated'])
localUpdateTime = parsedTime.astimezone(eastern).strftime("%a, %b %d at %I:%M%p")

# Write data to the forecast.json file
with open("forecast.json", "w") as forecastFile:
    json.dump(localForecastData, forecastFile, indent=2)
    forecastFile.close()

# Find the current forecast for the next coming Tuesday.
for day in localForecastData['properties']['periods']:
    if day['name'].lower() == 'tuesday':
        tuesdayForecast = day['detailedForecast']
        tuesdayDate = dateutil.parser.parse(day['startTime']).strftime("%A, %b %d")

print(f"Detailed Forecast for {tuesdayDate} (as of {localUpdateTime}): \n\n{tuesdayForecast}")

# Sources: 
# Notes from /Notes/week4june2.ipynb
# https://blog.bearer.sh/making-api-requests-with-python/
# weather.gov for API docs
# https://docs.python.org/3/library/datetime.html for datetime formatting
