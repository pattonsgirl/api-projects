# REST API + Database

## Environment Requirements
- python3
- Flask (`pip install Flask`)
- sqllite3 (should be packaged with python3 by default)

## Running code

- Start `Flask` application with `python3 api.py`
- By default, this will run a **listening** Flask application running on `localhost` on port `5000`
    - `http://127.0.0.1:5000` is the head hostname and destination port
- While application is running, logs of "caught" requests will display in the "output"
- Note: the `id` column lists all values as `null` in this sample database, so `id` based queries will return `[]` (empty)

## Basic functionality

- This REST API will refer to itself as `v2` in URL queries
- Uses a database running in SQLLite to query
- In order to find entries, the code will now run SQL queries on the database
- `@app.route` define which function are called based on the URL given
    - if `/` is queried, return landing page or API usage guide
    - if `/api/v2/resources/books/all` is queried, return JSON formatted list of data stored in dictionary
    - if `/api/v2/resources/books` is queried, it will check for an additional parameter (`?`) followed by a unique book id, the matching entry in the dictionary will be returned.
        - ex: `http://127.0.0.1:5000/api/v2/resources/books?author=Isaac+Asimov`
- `methods=['GET']` is a keyword argument that lets Flask know what kind of HTTP requests are allowed - we want to look at incoming `GET` data requests


## Basic usage

- Use a web browser or `curl` to send `GET` requests to the Flask application
- `http://127.0.0.1:5000/` returns a default page
- `http://127.0.0.1:5000/api/v2/resources/books/all` returns all items in database in JSON format
- `http://127.0.0.1:5000/api/v2/resources/books?author=Isaac+Asimov` returns item in database with `author` value of `Isaac Asimov` in JSON format
    - `published` is another valid query parameter
- Invalid queries that result in 404 resource not found will be returned an error message

## Resources
- [Programming Historian - Creating APIs with python and Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)
- [Auth0 - Developing RESTful APIs with python and Flask](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
