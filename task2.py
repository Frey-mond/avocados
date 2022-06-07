"""
CSE 163
Daniel Lee
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()


def yield_trend(data_yield):
    # Masks for avocado yield dataset
    is_2015_to_2018 = ((data_yield['Year'] >= 2015) &
                       (data_yield['Year'] <= 2018))
    is_Americas = (data_yield['Country or Area'] == 'Americas')
    is_Yield = (data_yield['Element'] == 'Yield')
    filtered_avo_yield = data_yield[is_2015_to_2018 & is_Americas & is_Yield]
    sns.relplot(x='Year', y='Value', kind='line', data=filtered_avo_yield)
    plt.title('Avocado Yield Trend Per Year From 2015 to 2018 (in hg/ha)')
    plt.savefig('./output/avocado_yield.png', bbox_inches='tight')


def sale_trend(data_sales):
    # Masks for avocado sales dataset
    is_US = (data_sales['region'] == 'TotalUS')
    is_2015_to_2018 = ((data_sales['year'] >= 2015) &
                       (data_sales['year'] <= 2018))
    is_conventional = ((data_sales['type'] == 'conventional') |
                       (data_sales['type'] == 'Conventional'))
    filtered_avo_sales = data_sales[is_US & is_2015_to_2018 & is_conventional]
    sns.relplot(x='year', y='AveragePrice', kind='line',
                data=filtered_avo_sales)
    plt.title('Average Price of an Avocado from 2015 to 2018')
    plt.savefig('./output/avocado_sales.png', bbox_inches='tight')


def apple_yield_trend(apple_data_yield):
    # Masks for apple sales dataset (should be same as avocado sales)
    is_2015_to_2018 = ((apple_data_yield['Year'] >= 2015) &
                       (apple_data_yield['Year'] <= 2018))
    is_Americas = (apple_data_yield['Country or Area'] == 'Americas')
    is_Yield = (apple_data_yield['Element'] == 'Yield')
    filtered_apple_yield = apple_data_yield[is_2015_to_2018
                                            & is_Americas & is_Yield]
    sns.relplot(x='Year', y='Value', kind='line', data=filtered_apple_yield)
    plt.title('Apple Yield Trend Per Year From 2015 to 2018 (in hg/ha)')
    plt.savefig('./output/apple_yield.png', bbox_inches='tight')


def main():
    avo_sales = pd.read_csv("./data/avocado cleaned.csv")
    avo_yield = pd.read_csv("./data/UNdata_Export_20220602_013049631.csv")
    apple_yield = pd.read_csv("./data/UNdata_Export_20220607_053812669.csv")
    sale_trend(avo_sales)
    yield_trend(avo_yield)
    apple_yield_trend(apple_yield)


if __name__ == '__main__':
    main()
