from flask import Flask, render_template, request
from sources import secret


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lastfm/')
def lastfm():
    return render_template('lastfm.html')

if __name__ == "__main__":
    app.run(debug =True)