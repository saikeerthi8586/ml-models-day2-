from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['Name'] = le.fit_transform(df['Name'])
df['Company'] = le.fit_transform(df['Company'])
df['City'] = le.fit_transform(df['City'])
df['Fuel_Type'] = le.fit_transform(df['Fuel_Type'])


X = df[['Name', 'Company', 'City', 'Year', 'KM_Driven',
        'No._of_Owners', 'Fuel_Type', 'Calculated_Score']]
y = df['On_Road_Price']


# training regression:
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)

# make predictions:
df['Predicted_Price'] = model.predict(X)
print(df)


