import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

"""
Built-in Themes in Seaborn:
darkgrid, whitegrid, dark, white, ticks
"""

# Sample data for theme demonstration
data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

# Theme examples
sns.set_theme(style='darkgrid')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='white')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='x', y='y', data=data)
plt.show()

# Custom theme
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})
sns.lineplot(x='x', y='y', data=data)
plt.show()


# ================================
# RealEstate-USA Dataset Section
# ================================

# Load dataset (UPDATED PATH + COLUMNS)
df = pd.read_csv(r'E:\DataSets_AI_Course\RealEstate-USA.csv')

print(df.dtypes)

# Take subsets
dffilter = df.head(40)
dffilter100 = df.head(100)

sns.set(style="whitegrid")


# ================================
# DISTRIBUTION PLOTS
# ================================

"""
Using:
x = city (categorical)
y = price (numeric)
hue = state (categorical)
"""

# Histogram (UPDATED columns)
g = sns.displot(data=dffilter, x="city", y="price", hue="state", kind='hist')
g.figure.suptitle("sns.displot(data=dffilter, x=city, y=price, hue=state, kind='hist')")
g.figure.show()
input("Wait for me....")


# KDE Plot (UPDATED columns)
"""
KDE works best with continuous variables
Using price vs house_size
"""
g = sns.displot(data=dffilter, x="price", y="house_size", kind='kde')
g.figure.suptitle("sns.displot(data=dffilter, x=price, y=house_size, kind='kde')")
g.figure.show()
input("Wait for me....")


# KDE single variable
g = sns.kdeplot(data=dffilter, x="price")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=price)")
g.figure.show()
input("Wait for me....")


# ================================
# HISTOGRAM
# ================================

g = sns.histplot(data=dffilter, x='city', y='price', hue='city', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='city', y='price', hue='city')")
g.figure.show()
input("Wait for me....")


# ================================
# SCATTER PLOT
# ================================

"""
Relationship between house size and price
"""
g = sns.scatterplot(x='house_size', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='house_size', y='price')")
g.figure.show()
input("Wait for me....")


# ================================
# LINE PLOT
# ================================

"""
Line plot is not ideal for categorical x,
but keeping logic same → using city
"""
g = sns.lineplot(data=dffilter, x="city", y="price")
g.figure.suptitle("sns.lineplot(data=dffilter, x=city, y=price)")
g.figure.show()
input("Wait for me....")


# ================================
# BAR PLOT
# ================================

g = sns.barplot(data=dffilter, x="city", y="price", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=city, y=price)")
g.figure.show()
input("Wait for me....")


# ================================
# CAT PLOT
# ================================

g = sns.catplot(data=dffilter, x="city", y="price")
g.figure.suptitle("sns.catplot(data=dffilter, x=city, y=price)")
g.figure.show()
input("Wait for me....")


# ================================
# HEATMAP
# ================================

"""
Pivot table for heatmap
columns = city
values = price
"""
glue = dffilter.pivot(columns="city", values="price")

g = sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue) - pivot(columns=city, values=price)")
g.figure.show()
input("Wait for me....")