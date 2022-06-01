"""
"""
import pickle
# import pandas as pd
# import geopandas as gpd
import plotly.express as px


def plot_total_volume():
    """
    """
    with open('./data/avocados_shp.df', 'rb') as f:
        data = pickle.load(f)
    # geo = gpd.read_file('./data/stanford-bx729wr3020-geojson.json')
    # data = data[data['year'] == 2020]

    # fig = px.choropleth_mapbox(
    #     data, geojson=geo.set_index('gnis_id').geometry,
    #     color='TotalVolume',
    #     locations='gnis_id',
    #     center={'lat': 39.0119, 'lon': -98.4842},
    #     mapbox_style='carto-positron',
    #     zoom=4
    # )
    fig = px.line(data, x=data.index, y='TotalVolume', color='region')
    fig.show()


def main():
    plot_total_volume()


if __name__ == '__main__':
    main()
