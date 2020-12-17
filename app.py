from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():

    today = datetime.now().strftime('%d-%b-%Y')

    continents = ['Asia','Africa','North America','South America',
    'Australia','Europe','Antartica']

    country_capital = {'India' : 'New Delhi',
    'USA' : 'Washington',
    'UAE' : 'Abu Dhabi'}

    return render_template("index.html",
    today = today,
    continents = continents,
    country_capital = country_capital)

if __name__ == "__main__":
    app.run(debug=True)