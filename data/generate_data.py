import pandas as pd
from sklearn.datasets import load_breast_cancer

def generate_data():
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    df.to_csv('data/data.csv', index=False)
    print('Data saved to data/data.csv')

if __name__ == '__main__':
    generate_data()
