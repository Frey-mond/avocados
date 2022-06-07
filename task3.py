"""
CSE 163
Eric Kim

This file implements task 3 as outlined in the report.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def avocados_for_a_home():
    # Creates Avocado Datasets for Detroit and San Fran
    avocado_data = pd.read_csv('./data/avocado cleaned.csv', na_values=['---'])
    avocado_data = avocado_data.rename(columns={'year': 'Year'})
    year_mask = avocado_data[(avocado_data['Year'] >= 2015) | (avocado_data['Year'] <= 2021)]
    san_fran_set = avocado_data[(avocado_data['region'] == 'SanFrancisco') & (year_mask)]
    detroit_set = avocado_data[(avocado_data['region'] == 'Detroit') & (year_mask)]
    san_fran_set = san_fran_set.groupby('Year')['AveragePrice'].mean().round(2)
    detroit_set = detroit_set.groupby('Year')['AveragePrice'].mean().round(2)
    # Creates Housing Dataset for Detroit and San Fran
    housing_data = pd.read_csv('./data/Zillow_House_Prices_Cleaned.csv', na_values=['---'])
    housing_data = housing_data[['Date', 'San Francisco, CA', 'Detroit, MI']]
    housing_data = housing_data.rename(columns={'San Francisco, CA': 'SanFrancisco', "Detroit, MI": "Detroit"})
    housing_data['Year'] = housing_data['Date'].str[-4:]
    housing_data = housing_data.groupby('Year').mean().round(2)
    print(housing_data)
    print(san_fran_set)
    # Plot 1
    
    # Plot 2
    AVG_AVOTST_PRC = 10


def main():
    avocados_for_a_home()


if __name__ == '__main__':
    main()