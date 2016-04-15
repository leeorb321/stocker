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


    def test_stock_ticker_details(self):
        ticker_symbol = 'AAPL'

        response = self.APP.get('/stock_ticker/AAPL')
        actual_response_body = str(response.data)

        self.assertIn(ticker_symbol, actual_response_body)
