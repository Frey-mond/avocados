"""
CSE 163
Eric Kim

This file implements task 3 as outlined in the report.
"""
import plotly.express as px


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
        title='Amount Saved from Avocado Abstinence vs '
        'House Prices in Detroit and San Francisco (2015-2021)'
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
        title='Amount Saved from Avocado Toast Abstinence vs '
        'House Prices in San Francisco (2015-2021)'
    )
    fig.add_bar(
        x=data['Year'],
        y=data['AvocadoToastExpenses'],
        name="Cumulative Avocado Expenditure"
    )
    fig.show()
