import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Iris dataset
iris = sns.load_dataset('iris')

# Histogram of sepal length
plt.hist(iris['sepal_length'], bins=10)
plt.title('Sepal Length Histogram')
plt.xlabel('Sepal Length')
plt.ylabel('Count')
plt.savefig('images/iris_sepal_length_hist.png')
plt.close()

# Bar chart: mean values per species
iris_mean = iris.groupby('species').mean()
iris_mean.plot(kind='bar')
plt.title('Mean Feature Values by Species')
plt.savefig('images/iris_mean_bar.png')
plt.close()

# Scatter plot: sepal length vs width
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.savefig('images/iris_sepal_scatter.png')
plt.close()

# Boxplot: petal width
sns.boxplot(x='species', y='petal_width', data=iris)
plt.savefig('images/iris_petal_box.png')
plt.close()

# Violin plots: sepal length and width
sns.violinplot(x='species', y='sepal_length', data=iris)
plt.savefig('images/iris_sepal_violin.png')
plt.close()

sns.violinplot(x='species', y='sepal_width', data=iris)
plt.savefig('images/iris_sepal_width_violin.png')
plt.close()

# Diamonds dataset
diamonds = sns.load_dataset('diamonds')

# Scatter plot: carat vs price
sns.scatterplot(x='carat', y='price', data=diamonds)
plt.savefig('images/diamonds_carat_price_scatter.png')
plt.close()

# Histogram: price with mean line
plt.hist(diamonds['price'], bins=30)
plt.axvline(diamonds['price'].mean(), color='red')
plt.savefig('images/diamonds_price_hist.png')
plt.close()

# Bar plot: count by cut
sns.countplot(x='cut', data=diamonds)
plt.savefig('images/diamonds_cut_count.png')
plt.close()

# Box plot: price by cut
sns.boxplot(x='cut', y='price', data=diamonds)
plt.savefig('images/diamonds_price_cut_box.png')
plt.close()

# Heatmap: numeric correlations
sns.heatmap(diamonds.corr(), annot=True)
plt.savefig('images/diamonds_heatmap.png')
plt.close()

# Line plot: average price per carat by cut
diamonds_avg = diamonds.groupby('cut').apply(lambda x: (x['price']/x['carat']).mean())
diamonds_avg.plot(kind='line')
plt.savefig('images/diamonds_avg_price_per_carat.png')
plt.close()
