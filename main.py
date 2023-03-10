import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential


cryppto_currency = 'BTC'

against_currency = 'PLN'

start = dt.datetime(2016,1,1)
end = dt.datetime.now()

data = web.DataReader(f'{cryppto_currency}-{against_currency}', 'yahoo', start, end)



print(data.head())

