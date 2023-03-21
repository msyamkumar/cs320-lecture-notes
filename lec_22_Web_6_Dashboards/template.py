import flask

# Notes for matplotlib.pyplot module
"""
fig, ax = plt.subplots(figsize=(3, 2)) enables us to create a new plot
fig.savefig(<file object>, format=<fig format>) enables us to save the figure into a file - default format is png
plt.close() closes most recent fig
plt.tight_layout() enables us to avoid cropping of the image
"""

# Notes for io module
"""
io.BytesIO for fake binary file
io.StringIO for fake text file
<fileobject>.getvalue() returns the content of the fake file
"""

# Notes for flask
"""
flask.request.args enables us process query string
@app.route("<URL>", methods=["POST"]) enables us to process HTTP POST requests
flask.request.get_data() enables us to access data (byte format) sent via HTTP POST request
"""

temps = [80, 85, 83, 90]

app = flask.Flask("my dashboard")

# DYNAMIC
@app.route("/")
def home():
    return """
    <html>
    <body bgcolor="Salmon">
    
    <h3>Example 1: PNG</h3>
    <img src="plot1.png">
    
    <h3>Example 2: SVG</h3>
    <img src="plot2.svg">
    
    </body>
    </html>
    """ 

# TODO: add route to plot1.png 
"""
IMPORTANT: file name and extension should match as in html content
Steps:
     1. generate a plot
     2. return the image contents:
         2a. v1: write and read from a temporary file
         2b. v2: use a fake file (io module)
     3. fix the content type: default content type is text/html: Content-Type: text/html
         3a. How can we find various content types? Google for "MIME types".
     4. IMPORTANT: close the figure. If this is not done, after 20 refreshes, you will start getting the below warning:
More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
     5. try to set y_label for the plot. This will not show up. 
     6. create a line plot with temps Series

"""

# TODO: add route to plot2.svg
"""
IMPORTANT: file name and extension should match as in html content
Things to change from plot1 function:
     1. Change content type
     2. Change format for savefig
     3. SVG files have text type (unlike PNG) - so we should use io.StringIO

"""

# TODO: add route for "/upload"
"""
Steps:
     1. support query string:
         - with key/parameter as temps and value as "," separated temperature values
         - add the values into temps list
     2. return len(temps)
     
Disadvantages of query string approach:
     1. If we have a lot of data, it is difficult to type. What if we are trying to upload a video?
     2. Caching:
         - memory of what we have already seen before; instead of slow web request, show what was already sent previously for the same request
         - browser cache
         - cache devices that sit in front of the server
         - server caching
         
Use POST request instead:
     1. Update route to add "methods=["POST"]"
     2. Humans don't send POST requests, instead we need to use "curl -X POST <URL> -d <data>" --- curl is a simple command line tool that enables us to send HTTP requests
     3. Use flask.request.get_data() - make sure to convert type to str
"""

# TODO: change SVG to histogram - very sensitive to number of "bins"
# TODO: change PNG to CDF (Cumulative Distribution Function):
"""
Idea: sort the data to observe some distribution, then switch x and y axes
Steps:
     1. sort the data
     2. switch x and y axes
     3. normalize the y axis from 0 to 100 - make sure to set ylim to 0
     4. change line plot "drawstyle" to "steps-post" - avoid extrapolating information between points

    s = pd.Series(sorted(temps))
    rev = pd.Series((s.index+1)/len(s)*100, index=s.values)
    rev.plot.line(ax=ax, ylim=0, drawstyle="steps-post")
"""

if __name__ == "__main__":
    # threaded must be False whenever we use matplotlib
    app.run(host="0.0.0.0", debug=True, threaded=False)

# app.run never returns, so don't define functions
# after this (the def lines will never be reached)
