import json

with open("forecast.json") as f:
    weekly_forecast = json.load(f)

properties = weekly_forecast["properties"]
#print(properties)

just_days = properties["periods"]
#print(just_days)

#for day in just_days:
#    print(day)
#    if day["name"] == "Tuesday":
#        print(day['detailedForecast'])

#properties = weekly_forecast["properties"]["periods"]

for day in just_days:
    if day["name"] == "Tuesday":
        print(day['detailedForecast'])
