from __future__ import division

from yahoo_finance import Share


def price_on_date(symbol, date):
    share = Share(symbol)
    share_data = share.get_historical(date,date)
    price = float(share_data[0]['Adj_Close'])
    return round(price,3)

def returns_per_share(symbol, from_date, to_date):
    buy_value = price_on_date(symbol,from_date)
    current_value = price_on_date(symbol,to_date)
    returns = (current_value - buy_value) / buy_value
    return round(returns,5)

def greatest_return(symbols, from_date, to_date):
    symbols_dict = {}
    for symbol in symbols:
        symbols_dict[symbol] = returns_per_share(
            symbol,
            from_date,
            to_date
        )
    return max(symbols_dict, key=symbols_dict.get)

def actual_returns(holdings, from_date, to_date):
    print sum(shares for holding, shares in holdings)
    return sum(shares for holding, shares in holdings)

    # result = 0
    # for holding in holdings:
    #     result += (price_on_date(holding, to_date) - price_on_date(holding, from_date)) * holdings[holding]
    # return round(result,3)

class StockQuote:
    def __init__(self, symbol):
        self.share = Share(symbol)

    def current_price(self):
        return self.share.get_price()
