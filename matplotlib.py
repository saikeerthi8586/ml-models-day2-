# preparing the target for matplotlib:
df['Is_Expensive'] = (df['On_Road_Price'] > 400000).astype(int)


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['Name'] = le.fit_transform(df['Name'])
df['Company'] = le.fit_transform(df['Company'])
df['City'] = le.fit_transform(df['City'])
df['Fuel_Type'] = le.fit_transform(df['Fuel_Type'])


# prepare x and y:
X = df[['Year', 'KM_Driven', 'No._of_Owners', 'Fuel_Type', 'Calculated_Score']]
y = df['Is_Expensive']


# Train Logistic Regression AND create y_pred
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X, y)

y_pred = model.predict(X)   # ← THIS LINE CREATES y_pred


print(y_pred[:5])


# matplotlib:
import matplotlib.pyplot as plt

df['Predicted_Is_Expensive'] = y_pred

plt.figure(figsize=(12, 6))
plt.plot(df['Is_Expensive'].values, label='Actual Is_Expensive')
plt.plot(df['Predicted_Is_Expensive'].values, label='Predicted Is_Expensive')
plt.legend()
plt.title('Actual vs Predicted (Logistic Regression)')
plt.xlabel('Index')
plt.ylabel('Class')
plt.show()


# KM_Driven vs Probability
y_prob = model.predict_proba(X)[:, 1]

plt.figure(figsize=(8, 5))
plt.scatter(df['KM_Driven'], y_prob)
plt.xlabel('KM Driven')
plt.ylabel('Probability of Expensive Car')
plt.title('KM Driven vs Probability (Logistic Regression)')
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df['Year'], y_prob)
plt.xlabel('Year')
plt.ylabel('Probability of Expensive Car')
plt.title('Year vs Probability')
plt.show()


# Calculated_Score vs Probability
plt.figure(figsize=(8, 5))
plt.scatter(df['Calculated_Score'], y_prob)
plt.xlabel('Calculated Score')
plt.ylabel('Probability of Expensive Car')
plt.title('Score vs Probability')
plt.show()
