import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df=pd.read_csv("data/heart.csv")
x=df.drop(columns=['target'])
y=df['target']

model=RandomForestClassifier()
model.fit(x,y)

joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")
