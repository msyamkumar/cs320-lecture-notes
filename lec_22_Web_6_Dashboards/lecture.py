import flask

app = flask.Flask("my dashboard")


# STATIC
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

if __name__ == "__main__":
    # threaded must be False whenever we use matplotlib
    app.run(host="0.0.0.0", debug=True, threaded=False)

# app.run never returns, so don't define functions
# after this (the def lines will never be reached)
