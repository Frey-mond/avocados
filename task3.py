"""
CSE 163
Eric Kim

This file implements task 3 as outlined in the report.
"""
import pandas as pd
import plotly.express as px


def avocados_for_a_home():
    """
    Formats and cleans the datasets for
    plot_avocados_for_a_house and
    plot_avocado_toast_for_a_house, returns
    the formatted dataset as Dataframe data.
    """
    # Formats Avocado Dataset
    avocado_data = pd.read_csv('./data/avocado cleaned.csv', na_values=['---'])
    avocado_data = avocado_data.rename(columns={'year': 'Year'})
    san_fran_mask = avocado_data['region'] == 'SanFrancisco'
    detroit_mask = avocado_data['region'] == 'Detroit'
    avocado_data = avocado_data[(san_fran_mask) | (detroit_mask)]
    avocado_data = avocado_data.groupby(
        'Year')['AveragePrice'].mean().round(2).reset_index()
    # Formats Housing Dataset
    housing_data = pd.read_csv('./data/Zillow_House_Prices_Cleaned.csv',
                               na_values=['---'])
    housing_data = housing_data[['Date', 'San Francisco, CA', 'Detroit, MI']]
    housing_data = housing_data.rename(columns={
                                        'San Francisco, CA': 'SanFrancisco',
                                        "Detroit, MI": "Detroit"
                                        })
    housing_data['Year'] = housing_data['Date'].str[-4:]
    housing_data['Year'] = pd.to_numeric(housing_data['Year'])
    housing_data = housing_data[(housing_data['Year'] >= 2015) &
                                (housing_data['Year'] <= 2021)]
    housing_data = housing_data[['Year', 'Detroit', 'SanFrancisco']]
    housing_data = housing_data.groupby(
        'Year')[['Detroit', 'SanFrancisco']].mean().round(2).reset_index()
    return avocado_data.merge(housing_data)


def plot_avocados_for_a_house(data):
    """
    Takes in Dataframe data and plots the average amount of
    money saved by not purchasing an avocado every day and compares
    the amount to the price of a house in Detroit and San
    Francisco. Amount saved determined by the average cost of an
    avocado from Detroit/San Francisco. Shows, but does not
    save the plot.
    """
    data['AnnualAvocadoExpenses'] = data['AveragePrice'] * 365
    data['AvocadoExpenses'] = data['AnnualAvocadoExpenses'].cumsum()
    fig = px.line(
        data,
        x='Year',
        y=['Detroit', 'SanFrancisco'],
        labels=dict(
            x='Year',
            variable='Legend',
            value='Cost',
            facet_col='variable'
        ),
        title='Amount Saved from Avocados vs. House Prices'
    )
    fig.add_bar(
        x=data['Year'],
        y=data['AvocadoExpenses'],
        name='Cumulative Avocado Expenditure'
    )
    fig.show()


def plot_avocado_toast_for_a_house(data):
    """
    Takes in Dataframe data and plots the average amount of
    money saved by not purchasing an avocado toast every day and compares
    the amount to the price of a house in San Francisco. Shows, but does not
    save the plot. Avocado toast price determined from online sources, adjusted
    for inflation.
    """
    AVG_AVOTST_PRC = 10.17
    data['AnnualAvocadoToastExpenses'] = 365 * AVG_AVOTST_PRC
    data['AvocadoToastExpenses'] = data['AnnualAvocadoToastExpenses'].cumsum()
    fig = px.line(
        x=data['Year'],
        y=data['SanFrancisco'],
        color=px.Constant('House Price'),
        labels=dict(x='Year', y='Cost', color='Legend'),
        title='Amount Saved from Avocado Toasts vs. House Prices'
    )
    fig.add_bar(
        x=data['Year'],
        y=data['AvocadoToastExpenses'],
        name="Cumulative Avocado Expenditure"
    )
    fig.show()
