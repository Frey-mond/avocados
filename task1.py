"""
CSE 163
Zachary Zhang

This files implements task 1 as outlined in the report.
"""
import pickle
import pandas as pd
import plotly.express as px


def plot_price_vs_volume():
    with open('./data/avocados_shp.df', 'rb') as f:
        data = pickle.load(f)

    data = data[data['region'] == 'TotalUS']

    average_price = data[['AveragePrice']].resample('M').mean()
    total_volume = data[['TotalVolume']].resample('M').sum()

    average_vs_total = pd.melt(
        average_price.merge(total_volume, on='Date'),
        ignore_index=False,
        value_vars=['AveragePrice', 'TotalVolume']
    )
    fig = px.line(
        average_vs_total,
        x=average_vs_total.index,
        y='value',
        color='variable',
        labels={
            'AveragePrice': 'Average Price Per Avocado($)',
            'Date': 'Date (Year)'
        },
        title='Average Avocado Price'
    )
    fig.show()


def plot_average_price():
    """
    Plots the Average Price of avocados by month.
    """
    with open('./data/avocados_shp.df', 'rb') as f:
        data = pickle.load(f)
    data = data[data['region'] == 'TotalUS']
    data = data[['AveragePrice']].resample('M').mean()
    fig = px.line(
        data, x=data.index,
        y='AveragePrice',
        labels={
            'AveragePrice': 'Average Price Per Avocado($)',
            'Date': 'Date (Year)'
        },
        title='Average Avocado Price'
    )
    fig.show()


def plot_total_volume():
    """
    Plots the total US avocado purchasing volume by month.
    """
    with open('./data/avocados_shp.df', 'rb') as f:
        data = pickle.load(f)
    data = data[data['region'] == 'TotalUS']
    data = data[['TotalVolume']].resample('M').sum()
    fig = px.line(
        data, x=data.index,
        y='TotalVolume',
        labels={
            'TotalVolume': 'Total Volume',
            'Date': 'Date (Year)'
        },
        title='Total US Avocado Volume'
    )
    fig.show()


def main():
    # plot_total_volume()
    # plot_average_price()
    plot_price_vs_volume()


if __name__ == '__main__':
    main()
