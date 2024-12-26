import pandas as pd  # Import the pandas library to work with data

# Load the dataset from a CSV file
df = pd.read_csv('iris.data.csv')

# Print the first 5 rows of the dataset to see what it looks like
print(df.head())
# Check the column names
print(df.columns)

# Display information about the dataset (number of rows, data types, etc.)
print(df.info())
# Rename columns to make them more understandable
df.columns = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

# Check the new column names
print(df.columns)
# Filter the dataset to include only rows where the Species is 'Iris-setosa'
setosa_df = df[df['Species'] == 'Iris-setosa']

# Display the first 5 rows of the filtered data
print(setosa_df.head())
# Group the data by Species and calculate the mean for each group
grouped_df = df.groupby('Species').mean()

# Print the grouped data
print(grouped_df)
# Perform aggregation to calculate mean and sum of SepalLength and SepalWidth
agg_df = df.groupby('Species').agg({
    'SepalLength': ['mean', 'sum'],
    'SepalWidth': ['mean', 'sum']
})

# Display the aggregated data
print(agg_df)
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot for SepalLength vs SepalWidth
sns.scatterplot(data=df, x='SepalLength', y='SepalWidth', hue='Species')

# Add a title to the plot
plt.title('Sepal Length vs Sepal Width by Species')

# Display the plot
plt.show()
# Create a box plot for Sepal Length across Species
sns.boxplot(x='Species', y='SepalLength', data=df)

# Add a title to the plot
plt.title('Distribution of Sepal Length by Species')

# Display the plot
plt.show()
