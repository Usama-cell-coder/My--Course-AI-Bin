"""
https://www.tutorialspoint.com/machine_learning/machine_learning_k_means_clustering.htm

Example 2
In this example, we are going to first generate 2D dataset containing 4 different blobs and after that will apply k-means algorithm to see the result.

First, we will start by importing the necessary packages −
"""
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.cluster import KMeans

"""
The following code will generate the 2D, containing four blobs −
"""

from sklearn.datasets import make_blobs
X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.60, random_state=0)
"""
Next, the following code will help us to visualize the dataset −
"""
plt.scatter(X[:, 0], X[:, 1], s=20);
plt.show()

"""
Visualizing 2D Blog
Next, make an object of KMeans along with providing number of clusters, train the model and do the prediction as follows −
"""

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

"""
Now, with the help of following code we can plot and visualize the cluster's centers picked by k-means Python estimator −
"""
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=20, cmap='summer')
centers = kmeans.cluster_centers_
color = np.array(['blue', 'hotpink', 'black', 'green'])

plt.scatter(centers[:, 0], centers[:, 1], c=color  , s=100, alpha=0.9);
plt.show()

wait = input("Hello")
