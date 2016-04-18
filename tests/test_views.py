import os
import unittest
from mock import patch

import requests

from stocker import app


class TestViews(unittest.TestCase):

    APP = app.test_client()

    def test_index(self):
        expected_index_page_text = 'stocker'

        response = self.APP.get('/')
        actual_response_body = str(response.data)

        self.assertIn(expected_index_page_text, actual_response_body)


    @patch('stocker.views.StockQuote')
    def test_stock_ticker_details(self, mock_stock_quote):
        ticker_symbol = 'AAPL'
        stock_price = 15.83
        mock_stock_quote.return_value.current_price.return_value = stock_price

        response = self.APP.get('/stock_ticker/' + ticker_symbol)
        actual_response_body = str(response.data)

        self.assertIn(ticker_symbol, actual_response_body)
        self.assertIn(str(stock_price), actual_response_body)

