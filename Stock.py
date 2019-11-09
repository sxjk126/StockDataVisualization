from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

key = 'UKBXLMP0KH34XX09'
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)
print("Stock Historic graph.")
userSymbol = ''
while (userSymbol != 'quit'):
    userSymbol = str(input("Type in the stock code for your desired stock historical quotes: ")).upper()
    stock_data, stock_meta_data = ts.get_daily(symbol=userSymbol)
    stock_sma, stock_meta_sma = ti.get_sma(symbol=userSymbol)
    figure(num=None, figsize=(15,6), dpi=80, facecolor='w', edgecolor='k')
    stock_data['4. close'].plot()
    plt.tight_layout()
    plt.grid()
    plt.show()


