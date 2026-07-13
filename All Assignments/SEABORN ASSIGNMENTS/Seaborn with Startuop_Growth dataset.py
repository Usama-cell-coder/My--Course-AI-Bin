import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# Load Dataset


df = pd.read_csv(r'E:\DataSets_AI_Course\startup_growth_investment_data.csv')

# Clean column names (VERY IMPORTANT)
df.columns = df.columns.str.strip()

print("Columns:", df.columns)
print(df.dtypes)
print(f"Dataset shape: {df.shape}")
print(f"Unique industries: {df['Industry'].nunique()}")

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Basic statistics
print("\nBasic statistics:\n", df.describe())

# Subsets for visualization
dffilter = df.head(40)
dffilter100 = df.head(100)

sns.set(style="whitegrid", palette="viridis")



# DISTRIBUTION PLOTS


"""
Mapping:
x = Industry (categorical)
y = Investment Amount (numeric)
hue = Country (categorical)
"""

# Displot for Investment Amount by Industry
g = sns.displot(data=dffilter, x="Industry", y="Investment Amount (USD)", hue="Country", kind='hist', height=6, aspect=1.5)
g.fig.suptitle("Displot: Industry vs Investment Amount (hue=Country)", y=1.02)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# KDE PLOT


"""
KDE for continuous variables
Using Investment Amount vs Valuation
"""

# 2D KDE
g = sns.displot(data=dffilter, x="Investment Amount (USD)", y="Valuation (USD)", kind='kde', height=6, aspect=1.2)
g.fig.suptitle("KDE: Investment Amount vs Valuation", y=1.02)
plt.show()

# KDE single variable - Investment Amount
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x="Investment Amount (USD)", fill=True, alpha=0.5)
plt.title("KDE Plot: Investment Amount Distribution")
plt.xlabel("Investment Amount (USD)")
plt.ylabel("Density")
plt.show()

# KDE single variable - Growth Rate
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x="Growth Rate (%)", fill=True, alpha=0.5, color='green')
plt.title("KDE Plot: Startup Growth Rate Distribution")
plt.xlabel("Growth Rate (%)")
plt.ylabel("Density")
plt.show()


# HISTOGRAM


# Histogram: Industry vs Investment Amount
plt.figure(figsize=(14, 6))
sns.histplot(data=dffilter, x='Industry', y='Investment Amount (USD)', hue='Industry', multiple="stack", legend=False)
plt.title("Histogram: Industry vs Investment Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram: Funding Rounds distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Funding Rounds', bins=20, kde=True)
plt.title("Distribution of Funding Rounds")
plt.xlabel("Number of Funding Rounds")
plt.ylabel("Count")
plt.show()



# SCATTER PLOT


"""
Relationship between Investment Amount and Valuation
"""

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Investment Amount (USD)', y='Valuation (USD)', data=dffilter, hue='Industry', size='Number of Investors', alpha=0.7)
plt.title("Scatter: Investment Amount vs Valuation (colored by Industry)")
plt.xlabel("Investment Amount (USD)")
plt.ylabel("Valuation (USD)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Scatter: Funding Rounds vs Growth Rate
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Funding Rounds', y='Growth Rate (%)', data=dffilter100, hue='Industry', alpha=0.7, s=100)
plt.title("Scatter: Funding Rounds vs Growth Rate")
plt.xlabel("Number of Funding Rounds")
plt.ylabel("Growth Rate (%)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()



# LINE PLOT


# Line plot: Year Founded vs Investment Amount (average by year)
yearly_avg = df.groupby('Year Founded')['Investment Amount (USD)'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_avg, x='Year Founded', y='Investment Amount (USD)', marker='o', linewidth=2)
plt.title("Line Plot: Average Investment Amount by Year Founded")
plt.xlabel("Year Founded")
plt.ylabel("Average Investment Amount (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Line plot: Country vs Average Valuation
country_valuation = df.groupby('Country')['Valuation (USD)'].mean().sort_values(ascending=False).head(15).reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=country_valuation, x='Country', y='Valuation (USD)', marker='o', linewidth=2, color='purple')
plt.title("Line Plot: Average Valuation by Country (Top 15)")
plt.xlabel("Country")
plt.ylabel("Average Valuation (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# BAR PLOT


# Bar plot: Industry vs Average Investment Amount
industry_investment = df.groupby('Industry')['Investment Amount (USD)'].mean().sort_values(ascending=False).reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(data=industry_investment, x='Industry', y='Investment Amount (USD)', palette='viridis')
plt.title("Bar Plot: Average Investment Amount by Industry")
plt.xlabel("Industry")
plt.ylabel("Average Investment Amount (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar plot: Top 10 Countries by Average Investment Amount
country_investment = df.groupby('Country')['Investment Amount (USD)'].mean().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(data=country_investment, x='Country', y='Investment Amount (USD)', palette='coolwarm')
plt.title("Bar Plot: Top 10 Countries by Average Investment Amount")
plt.xlabel("Country")
plt.ylabel("Average Investment Amount (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# CAT PLOT


# Catplot: Industry vs Growth Rate
g = sns.catplot(data=dffilter100, x="Industry", y="Growth Rate (%)", kind="box", height=6, aspect=1.5)
g.fig.suptitle("CatPlot (Box): Industry vs Growth Rate", y=1.02)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Catplot: Country vs Investment Amount (violin plot)
g = sns.catplot(data=df[df['Country'].isin(df['Country'].value_counts().head(8).index)], 
                x="Country", y="Investment Amount (USD)", kind="violin", height=6, aspect=1.5)
g.fig.suptitle("CatPlot (Violin): Country vs Investment Amount", y=1.02)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# HEATMAP


"""
Create correlation matrix for numerical columns
"""

# Select numerical columns for correlation
numerical_cols = ['Funding Rounds', 'Investment Amount (USD)', 'Valuation (USD)', 
                  'Number of Investors', 'Year Founded', 'Growth Rate (%)']

correlation_matrix = df[numerical_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, fmt='.2f')
plt.title("Heatmap: Correlation Matrix of Numerical Variables")
plt.tight_layout()
plt.show()

# Heatmap: Industry vs Average Investment Amount (pivot table)
industry_country_pivot = df.pivot_table(values='Investment Amount (USD)', 
                                         index='Industry', 
                                         columns='Country', 
                                         aggfunc='mean')

plt.figure(figsize=(14, 10))
sns.heatmap(industry_country_pivot, annot=True, cmap='YlOrRd', fmt='.0f', 
            linewidths=0.5, cbar_kws={'label': 'Average Investment Amount (USD)'})
plt.title("Heatmap: Average Investment Amount by Industry and Country")
plt.xlabel("Country")
plt.ylabel("Industry")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# ADDITIONAL INSIGHTFUL PLOTS


# Pairplot for selected numerical variables
selected_vars = ['Investment Amount (USD)', 'Valuation (USD)', 'Growth Rate (%)', 'Funding Rounds']
sample_df = df[selected_vars].sample(min(1000, len(df)))  # Sample for performance

sns.pairplot(sample_df, diag_kind='kde', plot_kws={'alpha': 0.5})
plt.suptitle("Pairplot: Relationships between Investment Metrics", y=1.02)
plt.show()

# Box plot: Funding Rounds distribution by Industry
plt.figure(figsize=(14, 6))
sns.boxplot(data=dffilter100, x='Industry', y='Funding Rounds', palette='Set3')
plt.title("Box Plot: Funding Rounds Distribution by Industry")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Count plot: Number of startups by Industry
plt.figure(figsize=(12, 6))
industry_counts = df['Industry'].value_counts()
sns.barplot(x=industry_counts.index, y=industry_counts.values, palette='pastel')
plt.title("Count Plot: Number of Startups by Industry")
plt.xlabel("Industry")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter plot with regression line: Number of Investors vs Investment Amount
plt.figure(figsize=(10, 6))
sns.regplot(data=df.sample(min(2000, len(df))), x='Number of Investors', y='Investment Amount (USD)', 
            scatter_kws={'alpha': 0.3}, line_kws={'color': 'red'})
plt.title("Regression Plot: Number of Investors vs Investment Amount")
plt.xlabel("Number of Investors")
plt.ylabel("Investment Amount (USD)")
plt.show()