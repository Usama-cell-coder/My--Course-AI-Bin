# GradientBoosting vs AdaBoost vs XGBoost vs CatBoost vs LightGBM
# https://www.geeksforgeeks.org/machine-learning/gradientboosting-vs-adaboost-vs-xgboost-vs-catboost-vs-lightgbm/


"""Gradient Boosting
Gradient Boosting is the boosting algorithm that works on the principle of the stagewise addition method, where multiple weak learning algorithms 
are trained and a strong learner algorithm is used as a final model from the addition of multiple weak learning algorithms trained on the same dataset."""

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split  
from sklearn.metrics import r2_score

X, y = make_regression(n_samples=100,
                       n_features=10,
                       n_informative=5,
                       n_targets=1,
                       random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
gbr = GradientBoostingRegressor()
gbr.fit(X_train, y_train)
y_pred1 = gbr.predict(X_test)
print("Gradient Boosting - R2: ",
      r2_score(y_test, y_pred1))

"""XGBoostpip
XGBoost is also a boosting machine learning algorithm, which is the next version on top of the gradient boosting algorithm. 
The full name of the XGBoost algorithm is the eXtreme Gradient Boosting algorithm, as the name suggests it is an extreme version 
of the previous gradient boosting algorithm.
pip install xgboost
"""

from xgboost import XGBRegressor
xgr = XGBRegressor()
xgr.fit(X_train, y_train)
y_pred2 = xgr.predict(X_test)
print("XGBoost - R2: ",
      r2_score(y_test, y_pred2))


"""AdaBoost
AdaBoost is a boosting algorithm, which also works on the principle of the stagewise addition method where multiple weak learners 
are used for getting strong learners. Unlike Gradient Boosting in XGBoost, the alpha parameter I calculated is related to the errors 
of the weak learner, here the value of the alpha parameter will be indirectly proportional to the error of the weak learner."""

from sklearn.ensemble import AdaBoostRegressor
adr = AdaBoostRegressor()
adr.fit(X_train, y_train)
y_pred3 = adr.predict(X_test)
print("AdaBoost - R2: ",
      r2_score(y_test, y_pred3))

"""CatBoost
In CatBoost the main difference that makes it different and better than others is the growing of decision trees in it. In CatBoost the decision trees which is grown are symmetric. One can easily install this library by using the below command:

pip install catboost"""

from catboost import CatBoostRegressor
cbr = CatBoostRegressor(iterations=100,
                        depth=5,
                        learning_rate=0.01,
                        loss_function='RMSE',
                        verbose=0)
cbr.fit(X_train, y_train)
y_pred4 = cbr.predict(X_test)
print("CatBoost - R2: ",
      r2_score(y_test, y_pred4))

"""LightGBM
LightGBM is also a boosting algorithm, which means Light Gradient Boosting Machine. It is used in the field of machine learning. In LightGBM decision trees are grown leaf wise meaning that at a single time only one leaf from the whole tree will be grown. One can install the required library by using the below command:

pip install lightgbm"""

import lightgbm as lgb
from lightgbm import LGBMRegressor
lgr = LGBMRegressor()
lgr.fit(X_train, y_train)
y_pred5 = lgr.predict(X_test)
print("LightGBM - R2: ",
      r2_score(y_test, y_pred5))

"""Comparison Between Different Boosting Algorithms
After fitting the data to the model, all of the algorithms return almost similar kind of results. Here LightGBM seems to perform poorly compared to other algorithms and XGBoost performs well in this case.

To visualize the performance of all the algorithms on the same data, we can also plot the graph between the y_test and y_pred of all the algorithms."""

import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots(figsize=(11, 5))

ax = sns.lineplot(x=y_test, y=y_pred1,
                  label='GradientBoosting')
ax1 = sns.lineplot(x=y_test, y=y_pred2,
                   label='XGBoost')
ax2 = sns.lineplot(x=y_test, y=y_pred3,
                   label='AdaBoost')
ax3 = sns.lineplot(x=y_test, y=y_pred4,
                   label='CatBoost')
ax4 = sns.lineplot(x=y_test, y=y_pred5,
                   label='LightGBM')

ax.set_xlabel('y_test', color='g')
ax.set_ylabel('y_pred', color='g')
fig.figure.show()

wait =  input("wait for....")