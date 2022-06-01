"""
CSE 163
Eric Kim

This file implements task 3 as outlined in the report.
"""
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def price_from_metric_model():
    avocado_data = pd.read_csv('./data/avocado cleaned.csv', na_values=['---'])
    metric_data = pd.read_csv('./data/f11ar cleaned.csv', na_values=['---'])
    print(avocado_data.head())
    print(metric_data.head())

def main():
    price_from_metric_model()


if __name__ == '__main__':
    main()