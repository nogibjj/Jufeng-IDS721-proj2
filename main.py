from flask import Flask
from flask import jsonify
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return "Hello World! CD"


@app.route("/echo/<name>")
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)

@app.route("/time")
def time():
    print("Print EST time")
    tz_NY = pytz.timezone('America/New_York') 
    datetime_NY = datetime.now(tz_NY)
    current_time_EST = datetime_NY.strftime("%H:%M:%S")
    return "Eastern Standard Time is " + current_time_EST


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
