from flask import render_template
from flask import request

from stocker import app
from stocker.stock_quote import StockQuote


@app.route('/', methods=['GET'])
def index():
    return "stocker main page"


@app.route('/stock_ticker/<ticker>', methods=['GET'])
def stock_ticker_details(ticker):
    calculated_price = StockQuote(symbol=ticker).current_price()
    return render_template('html/stock_ticker_details.html', ticker_symbol=ticker, current_price=calculated_price)
