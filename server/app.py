#!/usr/bin/env python3

import os

from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

# Component 1: Routing
@app.route('/')
def index():
    # Component 2: Request Handling
    host = request.headers.get('Host')  # Access the 'Host' header from the request

    # Component 3: Response Handling
    appname = current_app.name  # Access the name of the Flask application
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    status_code = 200
    headers = {}

    # Component 3: Response Handling
    return make_response(response_body, status_code, headers)

if __name__ == '__main__':
    # Component 7: Running the Development Server
    app.run(port=5555)
