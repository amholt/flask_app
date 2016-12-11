# Run a web server on our own computer!

# in terminal:
#	pip install flask
# 	python web.py
# in browser: 
#	http://127.0.0.1:5000/
#	http://127.0.0.1:5000/about.html
#	http://127.0.0.1:5000/?name=Anna


# If you make a change, you have to restart the server. 
#	Hit CTRL+C to close server, then re-run "python web.py" in the correct directory.

from flask import Flask, render_template, request
import weather
app = Flask(__name__)

@app.route("/")
def index():
    # request.values returns a dictionary, incl. any values of variable 'address'
    # add the .get so that you don't get an error if someone forgot to add it
    address = request.values.get('address')
    forecast = None
    if address:
    	forecast = weather.get_weather(address)
    # render_template loads template, & passes value of name through
    # 2nd forecast defined above,
    # 1st forecast is what it's called w/i template (use the same name)
    return render_template('index.html', forecast=forecast)

@app.route("/about.html")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()