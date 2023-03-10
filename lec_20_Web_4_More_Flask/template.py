import flask # requires installation if not already installed - pip3 install flask
import time
import json

app = flask.Flask("my application") # name of the web application can be anything

major_counts = {}
last_visit = 0 # TODO: dict of visit times, for each IP

# TODO: create a survey page
# flask.request.args: enables us to get the arguments passed as part of the URL
    
# TODO: create an add page

# TODO: create a never page

# TODO: create a robots.txt page
# flask.Response: enables us to create a response object instance
# 		  Arguments: str representing reponse, headers dict representing metadata

# TODO: create a slow page
# GOAL: don't let people visit this more often than once per 3s
# flask.request.remote_addr: enables us to take action based on the IP address from
#                            which we receive the request

# TODO: write code for creating a page for time.html
# TEMPLATE semi-static / semi-dynamic

# TODO: create a dynamic page ha.html
# DYNAMIC

# STATIC
# @ operator is called a "decorator"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=False)

# app.run never returns, so don't define functions
# after this (the def lines will never be reached)
