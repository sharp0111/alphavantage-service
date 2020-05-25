
'''
On your terminal run:
pip install alpha_vantage
This also uses the pandas dataframe, and matplotlib, commonly used python packages
pip install pandas
pip install matplotlib
For the develop version run:
pip install git+https://github.com/RomelTorres/alpha_vantage.git@develop
'''

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import os
from dotenv import load_dotenv
load_dotenv()


def main(symbol: str) -> None:
    # Your key here
    key = os.environ.get("ALPHAVANTAGE_KEY")
    # Chose your output format, or default to JSON (python dict)
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)

    # Get the data, returns a tuple
    # aapl_data is a pandas dataframe, aapl_meta_data is a dict
    stock_data, stock_meta_data = ts.get_daily(symbol)
    # aapl_sma is a dict, aapl_meta_sma also a dict
    stock_sma, stock_meta_sma = ti.get_sma(symbol)

    # Visualization
    figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
    stock_data['4. close'].plot()
    plt.tight_layout()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
