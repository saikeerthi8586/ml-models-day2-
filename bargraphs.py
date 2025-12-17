# bar graphs Average Price by Fuel Type (Seaborn)
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(
    x='Fuel_Type',
    y='On_Road_Price',
    data=df,
    estimator=sum
)
plt.title('Average On-Road Price by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Average Price')
plt.show()


# Bar Graph: Expensive vs Not Expensive Count (Matplotlib)
class_counts = df['Is_Expensive'].value_counts()

plt.figure()
plt.bar(class_counts.index.astype(str), class_counts.values)
plt.xlabel('Class (0 = Not Expensive, 1 = Expensive)')
plt.ylabel('Count')
plt.title('Count of Expensive vs Not Expensive Cars')
plt.show()


# Bar Graph: Average Calculated Score by Class
avg_score = df.groupby('Is_Expensive')['Calculated_Score'].mean()

plt.figure()
plt.bar(avg_score.index.astype(str), avg_score.values)
plt.xlabel('Is Expensive')
plt.ylabel('Average Calculated Score')
plt.title('Calculated Score by Class')
plt.show()


