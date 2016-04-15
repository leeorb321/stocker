from flask import render_template
from flask import request

from stocker import app


@app.route('/', methods=['GET'])
def index():
    return "stocker main page"


@app.route('/stock_ticker/<ticker>', methods=['GET'])
def stock_ticker_details(ticker):
    return render_template('html/stock_ticker_details.html', ticker_symbol=ticker)
