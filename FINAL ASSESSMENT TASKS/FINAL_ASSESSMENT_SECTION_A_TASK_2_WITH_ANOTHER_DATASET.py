# WORKING WITH SPACEX MISSION ANALYTICS
# IMPORTING LIBARARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report, silhouette_score
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings('ignore')
# LOADING DATASET
df = pd.read_csv(r'C:\Users\PMLS\Documents\GitHub\My_Course_AI_Bin\All DataSets\Final_Assessment_DataSets\SpaceX Missions, 2006\database.csv')
print("="*60)
print("SPACEX MISSION ANALYTICS")
print("="*60)
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns\n")
# DATA PREPROCESSING
print("DATA PREPROCESSING ")

# Clean column names
df.columns = df.columns.str.strip()

# Convert Launch Date to datetime
df['Launch Date'] = pd.to_datetime(df['Launch Date'], format='%d %B %Y', errors='coerce')
df['Year'] = df['Launch Date'].dt.year

# Clean numeric columns
df['Payload Mass (kg)'] = pd.to_numeric(df['Payload Mass (kg)'], errors='coerce')
df['Payload Mass (kg)'].fillna(df['Payload Mass (kg)'].median(), inplace=True)

# Create binary outcome (Success=1, Failure=0)
df['Mission_Success'] = df['Mission Outcome'].apply(lambda x: 1 if x == 'Success' else 0)

# Encode categorical variables
le_site = LabelEncoder()
le_vehicle = LabelEncoder()
le_payload = LabelEncoder()
le_orbit = LabelEncoder()
le_customer = LabelEncoder()
le_country = LabelEncoder()

df['Launch_Site_Encoded'] = le_site.fit_transform(df['Launch Site'].astype(str))
df['Vehicle_Encoded'] = le_vehicle.fit_transform(df['Vehicle Type'].astype(str))
df['Payload_Encoded'] = le_payload.fit_transform(df['Payload Type'].astype(str))
df['Orbit_Encoded'] = le_orbit.fit_transform(df['Payload Orbit'].astype(str))
df['Customer_Encoded'] = le_customer.fit_transform(df['Customer Name'].astype(str))
df['Country_Encoded'] = le_country.fit_transform(df['Customer Country'].astype(str))

print(f"Missing values filled: Payload Mass")
print(f"Categorical variables encoded: {len(df.columns)} features created")

# DESCRIPTIVE STATISSTICS WITH MAX OPERATIONS
print(" DESCRIPTIVE STATISTICS ")
print(df[['Payload Mass (kg)', 'Year']].describe())

print("\n--- MAX OPERATIONS ---")
print(f"Max Payload Mass: {df['Payload Mass (kg)'].max():.0f} kg")
print(f"Most Common Vehicle: {df['Vehicle Type'].mode().values[0]}")
print(f"Most Common Orbit: {df['Payload Orbit'].mode().values[0]}")
print(f"Max Missions per Year: {df['Year'].value_counts().max()} (Year: {df['Year'].value_counts().idxmax()})")
# INPUT DATA ANALYSIS WITH SEABORN
print(" GENERATING SEABORN VISUALIZATIONS ")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('SpaceX Mission Analytics: Input Data Analysis', fontsize=16)

# 1. Mission outcomes over time
outcome_by_year = df.groupby('Year')['Mission_Success'].agg(['count', 'sum'])
outcome_by_year['Failure'] = outcome_by_year['count'] - outcome_by_year['sum']
outcome_by_year[['sum', 'Failure']].plot(kind='bar', stacked=True, ax=axes[0,0])
axes[0,0].set_title('Mission Outcomes by Year')
axes[0,0].set_xlabel('Year')
axes[0,0].set_ylabel('Number of Missions')
axes[0,0].legend(['Success', 'Failure'])

# 2. Vehicle type distribution
df['Vehicle Type'].value_counts().head(10).plot(kind='barh', ax=axes[0,1])
axes[0,1].set_title('Top 10 Vehicle Types')
axes[0,1].set_xlabel('Count')

# HISTOGRAM
sns.histplot(df['Payload Mass (kg)'].dropna(), bins=20, kde=True, ax=axes[0,2])
axes[0,2].set_title('Payload Mass Distribution')
axes[0,2].set_xlabel('Payload Mass (kg)')

# 4. Orbit type distribution
df['Payload Orbit'].value_counts().plot(kind='pie', ax=axes[1,0], autopct='%1.1f%%')
axes[1,0].set_title('Orbit Type Distribution')
axes[1,0].set_ylabel('')

# 5. Success rate by country
country_success = df.groupby('Customer Country')['Mission_Success'].mean().sort_values(ascending=False).head(10)
country_success.plot(kind='bar', ax=axes[1,1])
axes[1,1].set_title('Success Rate by Country (Top 10)')
axes[1,1].set_xlabel('Country')
axes[1,1].set_ylabel('Success Rate')

# HEATMAP
corr_cols = ['Payload Mass (kg)', 'Year', 'Mission_Success', 'Launch_Site_Encoded', 'Vehicle_Encoded', 'Orbit_Encoded']
corr = df[corr_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[1,2])
axes[1,2].set_title('Correlation Heatmap')

plt.tight_layout()
plt.savefig('spacex_eda_plots.png', dpi=300, bbox_inches='tight')
print("Visualizations saved as 'spacex_eda_plots.png'")
plt.show()

# DATA PREPARATION


# Features for ML
features = ['Year', 'Payload Mass (kg)', 'Launch_Site_Encoded', 'Vehicle_Encoded',     'Payload_Encoded', 'Orbit_Encoded', 'Customer_Encoded', 'Country_Encoded']

X = df[features].copy()
y_reg = df['Payload Mass (kg)']  # Regression target
y_cls = df['Mission_Success']  # Classification target

# Handle missing values
imputer = SimpleImputer(strategy='median')
X_imputed = imputer.fit_transform(X)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

print(f"Feature matrix shape: {X_scaled.shape}")
print(f"Regression target shape: {y_reg.shape}")
print(f"Classification target shape: {y_cls.shape}")
print(f"Success Rate: {df['Mission_Success'].mean()*100:.1f}%")
# REGRESSION MODELS
print("\n" + "="*60)
print("REGRESSION ANALYSIS (Predicting Payload Mass)")
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


print(f"Linear Regression   - MSE: {mse_lr:.3f}, R²: {r2_lr:.3f}")
print(f"Random Forest Reg   - MSE: {mse_rf:.3f}, R²: {r2_rf:.3f}")
print(f"Gradient Boosting   - MSE: {mse_gb:.3f}, R²: {r2_gb:.3f}")

# Cross-validation
cv_scores = cross_val_score(rf_reg, X_scaled, y_reg, cv=5, scoring='r2')
print(f"\nRandom Forest CV R²: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")

# Feature importance
feature_importance = pd.DataFrame({   'Feature': features,   'Importance': rf_reg.feature_importances_
}).sort_values('Importance', ascending=False)
print("\nFeature Importance (Random Forest):")
print(feature_importance)

# CLASSIFICATION
print("\n" + "="*60)
print("CLASSIFICATION ANALYSIS (Predicting Mission Success)")
print("="*60)

X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(
    X_scaled, y_cls, test_size=0.2, random_state=42, stratify=y_cls
)

# Logistic Regression
log_reg = LogisticRegression(random_state=42, max_iter=1000)
log_reg.fit(X_train_cls, y_train_cls)
y_pred_log = log_reg.predict(X_test_cls)
acc_log = accuracy_score(y_test_cls, y_pred_log)

# Random Forest Classifier
rf_cls = RandomForestClassifier(n_estimators=100, random_state=42)
rf_cls.fit(X_train_cls, y_train_cls)
y_pred_rf_cls = rf_cls.predict(X_test_cls)
acc_rf = accuracy_score(y_test_cls, y_pred_rf_cls)


print(f"Logistic Regression Accuracy: {acc_log:.3f}")
print(f"Random Forest Accuracy: {acc_rf:.3f}")

# Cross-validation
cv_cls = cross_val_score(rf_cls, X_scaled, y_cls, cv=5, scoring='accuracy')
print(f"\nRandom Forest CV Accuracy: {cv_cls.mean():.3f} (+/- {cv_cls.std():.3f})")

# Classification report
y_pred_full = rf_cls.predict(X_scaled)
print("\nClassification Report:")
print(classification_report(y_cls, y_pred_full, target_names=['Failure', 'Success']))

# Feature importance for classification
cls_feature_importance = pd.DataFrame({   'Feature': features,   'Importance': rf_cls.feature_importances_
}).sort_values('Importance', ascending=False)
print("\nFeature Importance (Classification):")
print(cls_feature_importance)
# CLUSTERING

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
cluster_summary = df.groupby('Cluster').agg({   'Payload Mass (kg)': 'mean',   'Mission_Success': 'mean', 'Year': 'mean',    'Vehicle Type': lambda x: x.mode().iloc[0] if len(x) > 0 else 'Unknown',   'Payload Orbit': lambda x: x.mode().iloc[0] if len(x) > 0 else 'Unknown'
}).round(2)
cluster_summary.columns = ['Avg Payload Mass', 'Success Rate', 'Avg Year', 'Common Vehicle', 'Common Orbit']
print("\nCluster Summary:")
print(cluster_summary)

# Visualize clusters
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Clustering Results', fontsize=14)

# Cluster scatter plot
scatter = axes[0].scatter(df['Year'], df['Payload Mass (kg)'], c=df['Cluster'], cmap='viridis', s=100)
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Payload Mass (kg)')
axes[0].set_title('Clusters by Year vs Payload Mass')
plt.colorbar(scatter, ax=axes[0])

# Cluster by Success vs Payload
scatter2 = axes[1].scatter(df['Payload Mass (kg)'], df['Mission_Success'], c=df['Cluster'], cmap='viridis', s=100)
axes[1].set_xlabel('Payload Mass (kg)')
axes[1].set_ylabel('Mission Success (1=Success)')
axes[1].set_title('Clusters by Payload Mass vs Success')
plt.colorbar(scatter2, ax=axes[1])

plt.tight_layout()
plt.savefig('spacex_clustering_results.png', dpi=300, bbox_inches='tight')
print(" Clustering visualization saved as 'spacex_clustering_results.png'")
plt.show()

# ENSEMBLE LEARNING
print("\n" + "="*60)
print("ENSEMBLE LEARNING (Stacking Regressor & Classifier)")
print("="*60)

from sklearn.ensemble import StackingRegressor, StackingClassifier
from sklearn.svm import SVR, SVC

# Stacking Regressor
base_models_reg = [   ('rf', RandomForestRegressor(n_estimators=100, random_state=42)),   ('gb', GradientBoostingRegressor(n_estimators=100, random_state=42)),   ('svr', SVR(kernel='rbf'))
]

stacking_reg = StackingRegressor(estimators=base_models_reg, final_estimator=LinearRegression())
stacking_reg.fit(X_train, y_train)
y_pred_stack_reg = stacking_reg.predict(X_test)
mse_stack = mean_squared_error(y_test, y_pred_stack_reg)
r2_stack = r2_score(y_test, y_pred_stack_reg)

print(f"Stacking Regressor - MSE: {mse_stack:.3f}, R²: {r2_stack:.3f}")

# Stacking Classifier
base_models_cls = [
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('svc', SVC(kernel='rbf', probability=True, random_state=42))
]

stacking_cls = StackingClassifier(estimators=base_models_cls, final_estimator=LogisticRegression())
stacking_cls.fit(X_train_cls, y_train_cls)
y_pred_stack_cls = stacking_cls.predict(X_test_cls)
acc_stack = accuracy_score(y_test_cls, y_pred_stack_cls)

print(f"Stacking Classifier Accuracy: {acc_stack:.3f}")

# Model Comparison

print(f"Regression - Linear Regression    : R² = {r2_lr:.3f}")
print(f"Regression - Random Forest        : R² = {r2_rf:.3f}")
print(f"Regression - Gradient Boosting    : R² = {r2_gb:.3f}")
print(f"Regression - Stacking Ensemble    : R² = {r2_stack:.3f}")
print(f"\nClassification - Logistic Regression : {acc_log:.3f}")
print(f"Classification - Random Forest      : {acc_rf:.3f}")
print(f"Classification - Stacking Ensemble  : {acc_stack:.3f}")

# FINALIZING
print("\n" + "="*60)
print("FINAL ANALYSIS SUMMARY")
print("="*60)

# Success rate by year
yearly_success = df.groupby('Year')['Mission_Success'].mean() * 100
best_year = yearly_success.idxmax()
best_rate = yearly_success.max()

# Most common payload type
top_payload = df['Payload Type'].value_counts().index[0] if not df['Payload Type'].isna().all() else 'Unknown'

print(f"""
Key Findings:
1. Total Missions: {len(df)}
2. Overall Success Rate: {df['Mission_Success'].mean()*100:.1f}%
3. Best Year (Success Rate): {best_year} ({best_rate:.1f}%)
4. Most Common Vehicle: {df['Vehicle Type'].value_counts().index[0]}
5. Most Common Orbit: {df['Payload Orbit'].value_counts().index[0]}
6. Most Common Payload Type: {top_payload}
7. Average Payload Mass: {df['Payload Mass (kg)'].mean():.0f} kg
8. Max Payload Mass: {df['Payload Mass (kg)'].max():.0f} kg
9. Best Regression Model: {'Random Forest' if r2_rf > r2_gb else 'Gradient Boosting'} (R² = {max(r2_rf, r2_gb):.3f})
10. Best Classification Model: {'Stacking Classifier' if acc_stack > acc_rf else 'Random Forest'} (Accuracy = {max(acc_stack, acc_rf):.3f})
11. Clustering identified {len(cluster_summary)} distinct mission patterns
12. Ensemble Stacking Regressor achieved R² = {r2_stack:.3f}
""")

