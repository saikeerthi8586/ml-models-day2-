# seaborn KM_Driven vs Price (Colored by Class):
import seaborn as sns

sns.scatterplot(
    x='KM_Driven',
    y='On_Road_Price',
    hue='Is_Expensive',
    data=df
)
plt.title('KM Driven vs Price (Feature-Based)')
plt.show()


sns.boxplot(
    x='Is_Expensive',
    y='Calculated_Score',
    data=df
)
plt.title('Calculated Score vs Expensive Class')
plt.show()


# mutli feature view
sns.pairplot(
    df[['Year', 'KM_Driven', 'Calculated_Score', 'Is_Expensive']],
    hue='Is_Expensive'
)
plt.show()
