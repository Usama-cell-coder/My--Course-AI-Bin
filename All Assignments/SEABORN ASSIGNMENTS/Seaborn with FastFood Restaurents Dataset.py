import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

"""
Seaborn Built-in Themes:
darkgrid, whitegrid, dark, white, ticks
"""

# Sample data for theme demo
data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

# Theme demonstrations
sns.set_theme(style='darkgrid')
sns.lineplot(x='x', y='y', data=data)
plt.title("Theme: darkgrid")
plt.show()

sns.set_theme(style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.title("Theme: whitegrid")
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='x', y='y', data=data)
plt.title("Theme: dark")
plt.show()

sns.set_theme(style='white')
sns.lineplot(x='x', y='y', data=data)
plt.title("Theme: white")
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='x', y='y', data=data)
plt.title("Theme: ticks")
plt.show()

# Custom theme
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})
sns.lineplot(x='x', y='y', data=data)
plt.title("Custom Theme")
plt.show()



# FastFoodRestaurants Dataset


# Load dataset
df = pd.read_csv(r'E:\DataSets_AI_Course\FastFoodRestaurants.csv')

print(df.dtypes)

# Subsets
dffilter = df.head(40)
dffilter100 = df.head(100)

sns.set(style="whitegrid")



# DISTRIBUTION PLOTS


# Histogram
g = sns.displot(data=dffilter, x="city", y="latitude", hue="province", kind='hist')
g.fig.suptitle("Displot: city vs latitude (hue=state)")
plt.show()


# KDE Plot (continuous variables)
g = sns.displot(data=dffilter, x="latitude", y="longitude", kind='kde')
g.fig.suptitle("KDE: latitude vs longitude")
plt.show()


# KDE single variable
sns.kdeplot(data=dffilter, x="latitude")
plt.title("KDE Plot: latitude")
plt.show()



# HISTOGRAM


sns.histplot(data=dffilter, x='city', y='latitude', hue='city', multiple="stack")
plt.title("Histogram: city vs latitude")
plt.show()



# SCATTER PLOT


sns.scatterplot(x='longitude', y='latitude', data=dffilter)
plt.title("Scatter: longitude vs latitude")
plt.show()



# LINE PLOT


sns.lineplot(data=dffilter, x="city", y="latitude")
plt.title("Line Plot: city vs latitude")
plt.show()



# BAR PLOT


sns.barplot(data=dffilter, x="city", y="latitude")
plt.title("Bar Plot: city vs latitude")
plt.show()



# CAT PLOT


g = sns.catplot(data=dffilter, x="city", y="latitude")
g.fig.suptitle("CatPlot: city vs latitude")
plt.show()



# HEATMAP


# Pivot for heatmap
glue = dffilter.pivot(columns="city", values="latitude")

sns.heatmap(glue)
plt.title("Heatmap: city vs latitude")
plt.show()