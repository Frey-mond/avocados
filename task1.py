"""
CSE 163
Zachary Zhang

This files implements task 1 as outlined in the report.
"""
import pickle
import plotly.express as px


def plot_price_vs_volume(data):
    """
    Plots the Total Volume of Avocados vs the Average Price of Avocados
    """
    data = data.copy()
    data = data[data['region'] == 'TotalUS']
    data['type'] = data['type'].str.lower()
    data['TotalVolume'] = (data['TotalVolume'] / 1000000).round(2).copy()
    data['AveragePrice'] = data['AveragePrice'].round(2).copy()

    fig = px.scatter(
        data,
        x='AveragePrice',
        y='TotalVolume',
        labels={
            'AveragePrice': 'Average Avocado Price ($)',
            'TotalVolume': 'Total Volume (Million)'
        },
        facet_col='type',
        title='Average Price Vs. Total Volume'
    )
    fig.update_traces(
        hovertemplate='Average Price: $%{x} <br>Total Volume: %{y}M</br>'
    )
    fig.for_each_annotation(
        lambda a: a.update(
            text=a.text.split("=")[-1].capitalize() + ' Avocados'
        )
    )
    fig.show()


def plot_average_price(data):
    """
    Plots the Average Price of avocados by business quarter.
    """
    data = data.copy()
    data = data[data['region'] == 'TotalUS']
    data = data[['AveragePrice']].resample('BQ').mean().round(2).copy()

    fig = px.line(
        data, x=data.index,
        y='AveragePrice',
        labels={
            'AveragePrice': 'Average Price Per Avocado($)',
            'Date': 'Date (Year)'
        },
        title='Average Avocado Price Per Quarter',
        range_y=[0, 2]
    )
    fig.update_traces(
        mode='markers+lines', hovertemplate='Avocado Price: $%{y}'
    )
    fig.update_layout(hovermode='x unified')
    fig.show()


def plot_total_volume(data):
    """
    Plots the total US avocado purchasing volume by business quarter.
    """
    data = data.copy()
    data = data[data['region'] == 'TotalUS']
    data = data[['TotalVolume']].resample('BQ').sum()

    fig = px.line(
        data, x=data.index,
        y='TotalVolume',
        labels={
            'TotalVolume': 'Total Volume',
            'Date': 'Date (Year)'
        },
        title='Total US Avocado Volume Per Business Quarter',
        range_y=[0, 650000000]
    )
    fig.update_traces(mode='markers+lines', hovertemplate='Volume: %{y}')
    fig.update_layout(hovermode='x unified')
    fig.show()


def main():
    with open('./data/avocados_shp.df', 'rb') as f:
        data = pickle.load(f)
    plot_total_volume(data)
    plot_average_price(data)
    plot_price_vs_volume(data)


if __name__ == '__main__':
    main()
