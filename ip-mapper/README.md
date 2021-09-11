# IP Mapping Project

## Project Description:

Using the auth log from a standard ubuntu server configuration with no additional firewall configured, find out from where in the world connections to the server are being attempted and what the most common usernames are that attempt connection.

## Goals

1. Create a visualization that shows where ip addresses are coming from

2. Create a visualization that shows most common username attempts

## Where are the connections from?

![IP map plot](images/ip-markers.png)

### Discussion:

We can see connections are quite scattered.  This is expected given the prevalence of VPNs.  What it does tell me, from a security standpoint, is there are a lot of attempted connections that are /not/ from me / approved.  

## What are the most common user names?

![word cloud of usernames](images/username_wordcloud.png)

![bar chart of usernames](images/barchart-username.png)


### Discussion:

This did not end up as an impressive visualization, except perhaps to serve as a warning of services that commonly create admin accounts and may be exposed without being secured.

More useful are the statistics we can gather:

#### Top 10 usernames attempted:
- Username **admin** is used 79 times
- Username **user** is used 74 times
- Username **test** is used 28 times
- Username **oracle** is used 18 times
- Username **postgres** is used 15 times
- Username **pi** is used 15 times
- Username **mcserver** is used 15 times
- Username **minecraft** is used 14 times
- Username **jenkins** is used 12 times
- Username **hadoop** is used 11 times

## The code

- [ip_mapper.py](ip_mapper.py) uses [data/ip-latlons.csv](data/ip-latlons.csv) to gather ips and their corresponding lat / lon coordinates
    - Additional package: `plotly`
        - Installed with `conda install plotly`

- [username_charter.py](username_charter.py) focuses on finding the most commonly tested usernames.  Data for usernames is from [data/auth.logs.csv](data/auth.logs.csv)
    - Generates two visualizations 
        - a wordcloud of all usernames
        - a bar chart of the top ten usernames
    - Additional package: `wordcloud`
        - Installed with `pip install wordcloud`

- [ip_latlonfinder.py](ip_latlonfinder.py) uses an API (`ipinfo.io`) to trace the latitude and longitude of ip addresses.
    - Input is a csv file with `username, ip` as the format
    - Program parses for unique IP addresses
    - Program output is a `csv` placed in [data](data/ip-latlons.csv) called `ip-latlons.csv`
        - Output format: `ip, lat, lon`
    - The core code does not yet utilize pandas, but data is output in pandas friendly format

- [playground.ipynb](playground.ipynb) is a notebook that was used as a playground while deciding strategy for the project goal(s)