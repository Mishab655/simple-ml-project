import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import json
import os

os.makedirs('models', exist_ok=True)

df = pd.read_csv('data/data.csv')
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
preds = model.predict(X_test)

acc = accuracy_score(y_test, preds)
joblib.dump(model, 'models/model.pkl')

with open('models/metrics.json', 'w') as f:
    json.dump({'accuracy': acc}, f)

print(f'Model trained with accuracy: {acc:.4f}')
