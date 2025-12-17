import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


import pandas as pd
file_path = "/content/Car_Data.xlsx"
df = pd.read_excel(file_path)


df.head(5)

from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression

df['price_label'] = (df['On_Road_Price'] > df['On_Road_Price'].mean()).astype(int)

X = df[['KM_Driven']]
y = df['price_label']

model = LogisticRegression()
model.fit(X, y)

y_pred = model.predict(X)

cm = confusion_matrix(y, y_pred)
print(cm)

from sklearn.metrics import accuracy_score, precision_score

accuracy = accuracy_score(y, y_pred)
precision = precision_score(y, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
