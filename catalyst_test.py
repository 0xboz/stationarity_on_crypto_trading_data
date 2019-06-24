from catalyst.api import symbol, record
from catalyst import run_algorithm
import numpy as np
import pandas as pd
import stationarity_test


def initialize(context):
    context.asset = symbol('btc_usdt')


def handle_data(context, data):
    # The last known prices of current date and the day before
    yesterday_price, current_price = data.history(
        context.asset, 'price', 2, '1T')
    # Calculate return
    simple_return = current_price / yesterday_price
    # Calculate log return
    log_return = np.log(current_price) - np.log(yesterday_price)
    record(price=current_price, simple_return=simple_return, log_return=log_return)


def analyze(context, perf):
    sTest = stationarity_test.StationarityTests()
    # print(perf[['price', 'simple_return', 'log_return']].head())

    print('# Price Stationarity Testing')
    sTest.ADF_Test(perf.price)
    sTest.PP_Test(perf.price)
    sTest.KPSS_Test(perf.price)
    print('# Simple Return Stationarity Testing')
    sTest.ADF_Test(perf.simple_return)
    sTest.PP_Test(perf.simple_return)
    sTest.KPSS_Test(perf.simple_return)
    print('# Log Return Stationarity Testing')
    sTest.ADF_Test(perf.log_return)
    sTest.PP_Test(perf.log_return)
    sTest.KPSS_Test(perf.log_return)


if __name__ == '__main__':
    run_algorithm(capital_base=1000,
                  data_frequency='minute',
                  initialize=initialize,
                  handle_data=handle_data,
                  analyze=analyze,
                  exchange_name='poloniex',
                  quote_currency='usdt',
                  start=pd.to_datetime('2018-9-1', utc=True),
                  end=pd.to_datetime('2018-9-3', utc=True))
