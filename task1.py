"""
CSE 163
Zachary Zhang

This files implements task 1 as outlined in the report.
"""
import pickle
import plotly.express as px


def plot_total_volume():
    """
    Plots the total US avocado purchasing volume by month.
    """
    with open('./data/avocados_shp.df', 'rb') as f:
        data = pickle.load(f)
    data = data.resample('M').sum()
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
    plot_total_volume()


if __name__ == '__main__':
    main()
