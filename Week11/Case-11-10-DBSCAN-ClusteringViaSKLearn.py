"""
https://www.geeksforgeeks.org/machine-learning/dbscan-clustering-in-ml-density-based-clustering/

Implementation of DBSCAN Algorithm In Python 
Here we’ll use the Python library sklearn to compute DBSCAN and matplotlib.pyplot library for visualizing clusters.

Step 1: Importing Libraries 
We import all the necessary library like numpy , matplotlib and scikit-learn.
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn import datasets

"""Step 2: Preparing Dataset 
We will create a dataset of 4 clusters using make_blob. The dataset have 300 points that are grouped into 4 visible clusters.
"""
X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.50, random_state=0)
"""
Step 3: Applying DBSCAN Clustering
Now we apply DBSCAN clustering on our data, count it and visualize it using the matplotlib library.

eps=0.3: The radius to look for neighboring points.
min_samples: Minimum number of points required to form a dense region a cluster.
labels: Cluster numbers for each point. -1 means the point is considered noise.
"""
db = DBSCAN(eps=0.3, min_samples=10).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

unique_labels = set(labels)
colors = ['y', 'b', 'g', 'r']
print(colors)
for k, col in zip(unique_labels, colors):
    if k == -1:
       
        col = 'k'

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k',
             markersize=6)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k',
             markersize=6)

plt.title('number of clusters: %d' % n_clusters_)
plt.show()
"""
Output:

Cluster of dataset 
Cluster of dataset 
As shown in above output image cluster are shown in different colours like yellow, blue, green and red.

Step 4: Evaluation Metrics For DBSCAN Algorithm In Machine Learning 
We will use the Silhouette score and Adjusted rand score for evaluating clustering algorithms.

Silhouette's score is in the range of -1 to 1. A score near 1 denotes the best meaning that the data point i is very compact within the cluster to which it belongs and far away from the other clusters. The worst value is -1. Values near 0 denote overlapping clusters.
Absolute Rand Score is in the range of 0 to 1. More than 0.9 denotes excellent cluster recovery and above 0.8 is a good recovery. Less than 0.5 is considered to be poor recovery. 
"""
sc = metrics.silhouette_score(X, labels)
print("Silhouette Coefficient:%0.2f" % sc)
ari = metrics.adjusted_rand_score(y_true, labels)
print("Adjusted Rand Index: %0.2f" % ari)

"""
Output:

Coefficient:0.13
Adjusted Rand Index: 0.31:

"""