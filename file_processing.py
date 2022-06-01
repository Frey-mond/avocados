"""
"""
import pandas as pd
# import geopandas as gpd
import pickle


def avocados_processing():
    """
    """
    dataset = pd.read_csv(
        './data/avocado cleaned.csv', index_col='Date', parse_dates=True
    )
    # geo = gpd.read_file(
    #     './data/stanford-bx729wr3020-geojson.json'
    # )[['gnis_id', 'name']]
    # dataset_shp = dataset.merge(
    #     geo, left_on='region', right_on='name'
    # )
    # print(dataset.to_string())
    with open('./data/avocados_shp.df', 'wb') as f:
        pickle.dump(dataset, f)


def main():
    avocados_processing()


if __name__ == '__main__':
    main()
