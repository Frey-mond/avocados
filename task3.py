"""
CSE 163
Eric Kim

This file implements task 3 as outlined in the report.
"""
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def price_from_metric_model():
    # Formats data for model
    avocado_data = pd.read_csv('./data/avocado cleaned.csv', na_values=['---'])
    metric_data = pd.read_csv('./data/f11ar cleaned.csv', na_values=['---'])
    temp = avocado_data.groupby('year')['AveragePrice'].mean().round(2)
    data = metric_data.merge(temp, on='year', how='left')
    data = data.dropna()
    # Assigns features and labels
    features = data.loc[:, data.columns != 'AveragePrice']
    features = pd.get_dummies(features)
    labels = data['AveragePrice']
    # Runs Model
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2, shuffle=False)
    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    train_predictions = model.predict(features_train)
    test_predictions = model.predict(features_test)
    print('Training Mean Squared Error: ', mean_squared_error(labels_train, train_predictions))
    print('Test Mean Squared Error', mean_squared_error(labels_test, test_predictions))


def main():
    price_from_metric_model()


if __name__ == '__main__':
    main()