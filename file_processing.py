"""
CSE 163
Zachary Zhang

This file is used to perform joins and other
dataset modifcations accross multiple datasets.
"""
import pandas as pd
import pickle


def avocados_processing():
    """
    Used to modify 'avocados cleaned.csv'
    """
    data = pd.read_csv(
        './data/avocado cleaned.csv', index_col='Date', parse_dates=True
    )
    data['type'] = data['type'].str.capitalize()
    with open('./data/avocados_shp.df', 'wb') as f:
        pickle.dump(data, f)


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


def main():
    avocados_processing()
    avocados_for_a_home()


if __name__ == '__main__':
    main()
