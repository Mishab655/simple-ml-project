import joblib
import numpy as np

def predict(features):
    model = joblib.load('models/model.pkl')
    preds = model.predict(np.array(features))
    return preds.tolist()
