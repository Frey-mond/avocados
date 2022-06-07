"""
CSE 163
Eric Kim

This file implements task 3 as outlined in the report.
"""
import pandas as pd
import plotly.express as px


def avocados_for_a_home():
    """

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
    AVG_AVOTST_PRC = 10
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


def main():
    data = avocados_for_a_home()
    plot_avocados_for_a_house(data)
    plot_avocado_toast_for_a_house(data)


if __name__ == '__main__':
    main()
