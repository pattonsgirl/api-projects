# Basic REST API

## Environment Requirements
- python3
- Flask (`pip install Flask`)

## Running code

- Start `Flask` application with `python3 api.py`
- By default, this will run a **listening** Flask application running on `localhost` on port `5000`
    - `http://127.0.0.1:5000` is the head hostname and destination port

## Basic functionality

- Uses a python dictionary of entries as the data to query
- `@app.route` define which function are called based on the URL given
    - if `/` is queried, return landing page or API usage guide
    - if `/api/v1/resources/books/all` is queried, return JSON formatted list of data stored in dictionary
    - if `/api/v1/resources/books` is queried, it will check for an additional parameter (`?`) followed by a unique book id, the matching entry in the dictionary will be returned.
        - ex: `http://127.0.0.1:5000/api/v1/resources/books?id=1`
- `methods=['GET']` is a keyword argument that lets Flask know what kind of HTTP requests are allowed - we want to look at incoming `GET` data requests


## Basic usage

- Use a web browser or `curl` to send `GET` requests to the Flask application
- `http://127.0.0.1:5000/` returns a default page
- `http://127.0.0.1:5000/api/v1/resources/books/all` returns all items in dictionary in JSON format
- `http://127.0.0.1:5000/api/v1/resources/books?id=1` returns item in dictionary with `id` value of `1` in JSON format

## Resources
- [Programming Historian - Creating APIs with python and Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)
- [Auth0 - Developing RESTful APIs with python and Flask](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
