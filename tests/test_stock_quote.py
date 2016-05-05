import unittest
from mock import patch

# from yahoo_finance import Share

from stocker.stock_quote import *


class TestStockQuote(unittest.TestCase):
    GOOD_SYMBOL = 'AAPL'

    @patch('stocker.stock_quote.Share')
    def test_instantiates_yahoo_finance_share(self, mock_finance_wrapper):
        stock_quote = StockQuote(self.GOOD_SYMBOL)

        mock_finance_wrapper.assert_called_once_with(self.GOOD_SYMBOL)

    def test_price_on_date(self):
        value = price_on_date('AAPL', '2016-04-12')

        self.assertEqual(value, 110.44)


    @patch('stocker.stock_quote.price_on_date')
    def test_returns(self, mock_price_on_date):
        mock_price_on_date.side_effect = [2000, 2500]

        value = returns_per_share(
            symbol='AAPL',
            from_date='2015-01-01',
            to_date='2016-02-02'
        )

        self.assertEqual(value, 0.25)

    # @patch('stocker.stock_quote.returns_per_share')
    def test_greatest_returns(self):
        stocks_to_compare = ['AAPL', 'GOOG', 'AMZN']
        from_date = '2015-01-02'
        to_date = '2015-09-03'

        best_stock = greatest_return(
            stocks_to_compare,
            from_date,
            to_date
        )

        self.assertEqual(best_stock, 'AMZN')


    def test_actual_returns(self):
        holdings = {'AMZN': 5,'AAPL': 5}

        from_date = '2015-01-02'
        to_date = '2015-09-03'

        ROI = actual_returns(
            holdings,
            from_date,
            to_date
        )

        self.assertEqual(ROI, 992.94)

    # @patch('stocker.stock_quote.yahoo_finance')
    # def test_current_price(self, mock_stock_library):
    #     mock_stock_library.Share.return_value
    #     stock_quote = StockQuote(self.GOOD_SYMBOL)
    #     expected_price

    #     actual_price = stock_quote.current_price()

    #     self.assertEqual(actual_price, expected_price)

