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
    plt.title('Yield Trend Per Year From 2015 to 2018')
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def sale_trend(data_sales):
    # Masks for avocado sales dataset
    is_US = (data_sales['region'] == 'TotalUS')
    is_2015_to_2018 = ((data_sales['year'] >= 2015) &
                       (data_sales['year'] <= 2018))
    is_conventional = ((data_sales['type'] == 'conventional') |
                       (data_sales['type'] == 'Conventional'))
    filtered_avo_sales = data_sales[is_US & is_2015_to_2018 & is_conventional]
    print(filtered_avo_sales)
    """
    sns.relplot(x='year', y='Yield', kind='line', data=filtered_avo_sales)
    plt.title('Yield Trend Per Year From 2015 to 2018')
    plt.savefig('line_plot_bachelors2.png', bbox_inches='tight')
    """


def main():
    avo_sales = pd.read_csv("./data/avocados cleaned.csv")
    avo_yield = pd.read_csv("./data/UNdata_Export_20220602_013049631.csv")
    yield_trend(avo_yield)
    sale_trend(avo_sales)


if __name__ == '__main__':
    main()
