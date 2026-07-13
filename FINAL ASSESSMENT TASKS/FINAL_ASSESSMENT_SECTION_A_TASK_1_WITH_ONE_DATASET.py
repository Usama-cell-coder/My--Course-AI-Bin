# BISMILLAH
# Working on NASA_ANALYTICS_2010-2020
# Importing Libararies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report, silhouette_score
import warnings
warnings.filterwarnings('ignore')

# Loading DataSet
df = pd.read_csv(r'C:\Users\PMLS\Documents\GitHub\My_Course_AI_Bin\All DataSets\Final_Assessment_DataSets\Space_Industry_Analytics\Nasa_Analytics_2010_2024.csv')
print("="*60)
print("NASA ANALYTICS (2010-2024)")
print("="*60)
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns\n")

# Performing Descriptive Statistics with Max Operations


print(df.describe())

print(" MAX OPERATIONS")
print(f"Max Launches: {df['Launches'].max()} (Year: {df[df['Launches'] == df['Launches'].max()]['Year'].values[0]})")
print(f"Max Employees: {df['Employees'].max()} (Year: {df[df['Employees'] == df['Employees'].max()]['Year'].values[0]})")
print(f"Max Budget: ${df['Budget_Funding_USD_M'].max()}M (Year: {df[df['Budget_Funding_USD_M'] == df['Budget_Funding_USD_M'].max()]['Year'].values[0]})")
print(f"Max Rockets: {df['Rockets'].max()} (Year: {df[df['Rockets'] == df['Rockets'].max()]['Year'].values[0]})")

# Input Data Analysis with Seaborn
print("\n--- GENERATING SEABORN VISUALIZATIONS ---")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('NASA Analytics: Input Data Analysis', fontsize=16)

# Creating LinePlot
sns.lineplot(data=df, x='Year', y='Launches', marker='o', ax=axes[0,0])
axes[0,0].set_title('Launches Over Time')
axes[0,0].grid(True)

# Creating BarPlot
sns.barplot(data=df, x='Year', y='Budget_Funding_USD_M', ax=axes[0,1])
axes[0,1].set_title('Budget Funding Over Time')
axes[0,1].tick_params(axis='x', rotation=45)


sns.lineplot(data=df, x='Year', y='Employees', marker='s', color='green', ax=axes[0,2])
axes[0,2].set_title('Employees Over Time')
axes[0,2].grid(True)

# Creating Correlation Heatmap
corr = df[['Launches', 'Budget_Funding_USD_M', 'Employees', 'Rockets']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[1,0])
axes[1,0].set_title('Correlation Heatmap')

# Scatter Plot
sns.scatterplot(data=df, x='Budget_Funding_USD_M', y='Launches', size='Employees', hue='Year', ax=axes[1,1])
axes[1,1].set_title('Budget vs Launches (size=Employees)')
# Creating Histogram
sns.histplot(df['Rockets'], bins=3, kde=True, ax=axes[1,2])
axes[1,2].set_title('Rockets Distribution')

plt.tight_layout()
plt.savefig('nasa_eda_plots.png', dpi=300, bbox_inches='tight')
print("Visualizations saved as 'nasa_eda_plots.png'")
plt.show()

# Data Preparation for Machine Learning

X = df[['Year', 'Budget_Funding_USD_M', 'Employees', 'Rockets']].copy()
y_reg = df['Launches']  # Regression target

df['Launch_Category'] = (df['Launches'] > 7).astype(int)
y_cls = df['Launch_Category']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"Feature matrix shape: {X_scaled.shape}")
print(f"Regression target shape: {y_reg.shape}")
print(f"Classification target shape: {y_cls.shape}")
print(f"Class distribution: {df['Launch_Category'].value_counts().to_dict()}")
# Regression Models
print("\n" + "="*60)
print("REGRESSION ANALYSIS (Predicting Launches)")
print("="*60)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_reg, test_size=0.2, random_state=42)

# Model 1: Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

# Model 2: Random Forest Regressor
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X_train, y_train)
y_pred_rf = rf_reg.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

# Model 3: Gradient Boosting Regressor
gb_reg = GradientBoostingRegressor(n_estimators=100, random_state=42)
gb_reg.fit(X_train, y_train)
y_pred_gb = gb_reg.predict(X_test)
mse_gb = mean_squared_error(y_test, y_pred_gb)
r2_gb = r2_score(y_test, y_pred_gb)

print("REGRESSION METRICS")
print(f"Linear Regression   - MSE: {mse_lr:.3f}, R²: {r2_lr:.3f}")
print(f"Random Forest Reg   - MSE: {mse_rf:.3f}, R²: {r2_rf:.3f}")
print(f"Gradient Boosting   - MSE: {mse_gb:.3f}, R²: {r2_gb:.3f}")

# Cross-validation for best model
cv_scores = cross_val_score(rf_reg, X_scaled, y_reg, cv=5, scoring='r2')
print(f"\nRandom Forest CV R²: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")

# Feature importance
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_reg.feature_importances_
}).sort_values('Importance', ascending=False)
print("\nFeature Importance (Random Forest):")
print(feature_importance)

# Classification

print("\n" + "="*60)
print("CLASSIFICATION ANALYSIS (High vs Low Launches)")
print("="*60)

X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(
    X_scaled, y_cls, test_size=0.2, random_state=42
)

# Logistic Regression
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train_cls, y_train_cls)
y_pred_log = log_reg.predict(X_test_cls)
acc_log = accuracy_score(y_test_cls, y_pred_log)

# Random Forest Classifier
rf_cls = RandomForestClassifier(n_estimators=100, random_state=42)
rf_cls.fit(X_train_cls, y_train_cls)
y_pred_rf_cls = rf_cls.predict(X_test_cls)
acc_rf = accuracy_score(y_test_cls, y_pred_rf_cls)

print(" CLASSIFICATION METRICS ")
print(f"Logistic Regression Accuracy: {acc_log:.3f}")
print(f"Random Forest Accuracy: {acc_rf:.3f}")

# Cross-validation
cv_cls = cross_val_score(rf_cls, X_scaled, y_cls, cv=5, scoring='accuracy')
print(f"\nRandom Forest CV Accuracy: {cv_cls.mean():.3f} (+/- {cv_cls.std():.3f})")

# Classification report
y_pred_full = rf_cls.predict(X_scaled)
print("\nClassification Report (Full Dataset):")
print(classification_report(y_cls, y_pred_full, target_names=['Low Launches', 'High Launches']))
# Clustering
print("\n" + "="*60)
print("CLUSTERING ANALYSIS")
print("="*60)

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Silhouette score
sil_score = silhouette_score(X_scaled, df['Cluster'])
print(f"Silhouette Score (3 clusters): {sil_score:.3f}")

# Cluster analysis
cluster_summary = df.groupby('Cluster').agg({
    'Year': 'count',
    'Launches': 'mean',
    'Budget_Funding_USD_M': 'mean',
    'Employees': 'mean',
    'Rockets': 'mean'
}).round(1)
cluster_summary.columns = ['Count', 'Avg Launches', 'Avg Budget', 'Avg Employees', 'Avg Rockets']
print("\nCluster Summary:")
print(cluster_summary)

# Visualize clusters
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Clustering Results', fontsize=14)

# Cluster scatter plot
scatter = axes[0].scatter(df['Year'], df['Launches'], c=df['Cluster'], cmap='viridis', s=100)
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Launches')
axes[0].set_title('Clusters by Year vs Launches')
plt.colorbar(scatter, ax=axes[0])

# Cluster by Budget
scatter2 = axes[1].scatter(df['Budget_Funding_USD_M'], df['Employees'], c=df['Cluster'], cmap='viridis', s=100)
axes[1].set_xlabel('Budget (USD M)')
axes[1].set_ylabel('Employees')
axes[1].set_title('Clusters by Budget vs Employees')
plt.colorbar(scatter2, ax=axes[1])

plt.tight_layout()
plt.savefig('nasa_clustering_results.png', dpi=300, bbox_inches='tight')
print(" Clustering visualization saved as 'nasa_clustering_results.png'")
plt.show()
# Ensemble Learning
print("\n" + "="*60)
print("ENSEMBLE LEARNING (Stacking Regressor)")
print("="*60)

from sklearn.ensemble import StackingRegressor
from sklearn.svm import SVR

# Define base estimators
base_models = [
    ('rf', RandomForestRegressor(n_estimators=100, random_state=42)),
    ('gb', GradientBoostingRegressor(n_estimators=100, random_state=42)),
    ('svr', SVR(kernel='rbf'))
]

# Stacking regressor
stacking_reg = StackingRegressor(estimators=base_models, final_estimator=LinearRegression())
stacking_reg.fit(X_train, y_train)
y_pred_stack = stacking_reg.predict(X_test)

mse_stack = mean_squared_error(y_test, y_pred_stack)
r2_stack = r2_score(y_test, y_pred_stack)

print(f"Stacking Regressor - MSE: {mse_stack:.3f}, R²: {r2_stack:.3f}")

# Compare all models
print(" MODEL COMPARISON ")
print(f"Linear Regression    : R² = {r2_lr:.3f}")
print(f"Random Forest        : R² = {r2_rf:.3f}")
print(f"Gradient Boosting    : R² = {r2_gb:.3f}")
print(f"Stacking Ensemble    : R² = {r2_stack:.3f}")

# Finalizing

print("\n" + "="*60)
print("FINAL ANALYSIS SUMMARY")
print("="*60)

print(f"""
Key Findings:
1. Launches increased from {df['Launches'].min()} in {df[df['Launches'] == df['Launches'].min()]['Year'].values[0]} 
   to {df['Launches'].max()} in {df[df['Launches'] == df['Launches'].max()]['Year'].values[0]}
2. Budget grew from ${df['Budget_Funding_USD_M'].min()}M to ${df['Budget_Funding_USD_M'].max()}M
3. Employees increased from {df['Employees'].min()} to {df['Employees'].max()}
4. Success rate remained at 100% throughout
5. Best Regression Model: {'Random Forest' if r2_rf > r2_gb else 'Gradient Boosting'} (R² = {max(r2_rf, r2_gb):.3f})
6. Best Classification Accuracy: {max(acc_log, acc_rf):.3f}
7. Clustering identified {len(cluster_summary)} distinct operational phases
8. Ensemble Stacking achieved R² = {r2_stack:.3f}
""")

