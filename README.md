# API Sample Repo

## parse-json

Folder includes parsers to from API requests.

These parsers rely on the API request already being done, then used in the code

## ip-mapper

Folder includes README.md with more details.  Basic gist is project takes an input file of attempted connection logs to a server.  Code parses this to username & IP address.  

The IP address is queried via ipinfo.io, which returns known origin info about the IP address - namely lat/lon coordinates.

Saving these off, the code then maps them (the coordinates) to a global map.

## restapi

Uses flask to serve content over port 5000 on localhost

api code iteself contains the information to query (in list form)

Investigate this code to explore how REST API requests parse URLs for query information

## restapi_w_db

Uses flask to serve content over port 5000 on localhost

Uses sqlite3 with a book database

api code contains how the databse is queried by parsing the URLs for query information and translating into a standard SQL query
