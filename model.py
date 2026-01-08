import joblib
import numpy as np

class heart_model:
    def __init__(self):
        self.model = joblib.load("model.pkl")

    def predict(self, features):
        input_data = np.array([features])
        prediction = self.model.predict(input_data)
        return "Heart Disease" if prediction[0] == 1 else "No Heart Disease"
