import pandas as pd

def load_data(path):
    data = pd.read_csv(path)
    X = data[['Hours']]
    y = data['Marks']
    return X, y
