"""
CSE 163
Eric Kim, Daniel Lee, Zachary Zhang

Runs the different tasks to generate the data used in report.md
"""
import file_processing
import task_1
import task_2
import task_3

import pickle
import pandas as pd


def main():
    with open('./data/avocados_shp.df', 'rb') as f:
        data = pickle.load(f)
    task_1.plot_total_volume(data)
    task_1.plot_average_price(data)
    task_1.plot_price_vs_volume(data)
    task_1.plot_seattle(data)

    avo_sales = pd.read_csv("./data/avocado cleaned.csv")
    avo_yield = pd.read_csv("./data/UNdata_Export_20220602_013049631.csv")
    apple_yield = pd.read_csv("./data/UNdata_Export_20220607_053812669.csv")
    task_2.sale_trend(avo_sales)
    task_2.yield_trend(avo_yield)
    task_2.apple_yield_trend(apple_yield)

    data3 = file_processing.avocados_for_a_home()
    task_3.plot_avocados_for_a_house(data3)
    task_3.plot_avocado_toast_for_a_house(data3)


if __name__ == '__main__':
    main()
