import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# Load Dataset

df = pd.read_csv(r'E:\DataSets_AI_Course\Real_Estate_Sales_2001-2022_GL-Short.csv')

# Clean column names (VERY IMPORTANT)
df.columns = df.columns.str.strip()

print("Columns:", df.columns)
print(df.dtypes)

# Subsets
dffilter = df.head(40)
dffilter100 = df.head(100)

sns.set(style="whitegrid")



# DISTRIBUTION PLOTS


"""
Mapping:
x = Town (categorical)
y = Sale Amount (numeric)
hue = Property Type (categorical)
"""

g = sns.displot(data=dffilter, x="Town", y="Sale Amount", hue="Property Type", kind='hist')
g.fig.suptitle("Displot: Town vs Sale Amount (hue=Property Type)")
plt.show()


# KDE PLOT


"""
KDE requires continuous variables
Using Assessed Value vs Sale Amount
"""

g = sns.displot(data=dffilter, x="Assessed Value", y="Sale Amount", kind='kde')
g.fig.suptitle("KDE: Assessed Value vs Sale Amount")
plt.show()


# KDE single variable
sns.kdeplot(data=dffilter, x="Sale Amount")
plt.title("KDE Plot: Sale Amount")
plt.show()


# HISTOGRAM


sns.histplot(data=dffilter, x='Town', y='Sale Amount', hue='Town', multiple="stack")
plt.title("Histogram: Town vs Sale Amount")
plt.show()



# SCATTER PLOT


"""
Relationship between Assessed Value and Sale Amount
"""

sns.scatterplot(x='Assessed Value', y='Sale Amount', data=dffilter)
plt.title("Scatter: Assessed Value vs Sale Amount")
plt.show()



# LINE PLOT


sns.lineplot(data=dffilter, x="Town", y="Sale Amount")
plt.title("Line Plot: Town vs Sale Amount")
plt.show()


# BAR PLOT


sns.barplot(data=dffilter, x="Town", y="Sale Amount")
plt.title("Bar Plot: Town vs Sale Amount")
plt.show()



# CAT PLOT


g = sns.catplot(data=dffilter, x="Town", y="Sale Amount")
g.fig.suptitle("CatPlot: Town vs Sale Amount")
plt.show()


# HEATMAP

"""
Pivot for heatmap:
columns = Town
values = Sale Amount
"""

glue = dffilter.pivot(columns="Town", values="Sale Amount")

sns.heatmap(glue)
plt.title("Heatmap: Town vs Sale Amount")
plt.show()