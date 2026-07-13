"""
https://www.tutorialspoint.com/machine_learning/machine_learning_k_means_clustering.htm

Example 3
Let us move to another example in which we are going to apply K-means clustering on simple digits dataset. K-means will try to identify similar digits without using the original label information.

First, we will start by importing the necessary packages −
"""
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.cluster import KMeans

#Next, load the digit dataset from sklearn and make an object of it. We can also find number of rows and columns in this dataset as follows −

from sklearn.datasets import load_digits
digits = load_digits()
print("digits.data.shape: ", digits.data.shape)
"""
Output
(1797, 64)

The above output shows that this dataset is having 1797 samples with 64 features.

We can perform the clustering as we did in Example 1 above −
"""
kmeans = KMeans(n_clusters=10, random_state=0)
clusters = kmeans.fit_predict(digits.data)
kmeans.cluster_centers_.shape
print("kmeans.cluster_centers_.shape: " , kmeans.cluster_centers_.shape)
"""
Output
(10, 64)
The above output shows that K-means created 10 clusters with 64 features.
"""
fig, ax = plt.subplots(2, 5, figsize=(8, 3))
centers = kmeans.cluster_centers_.reshape(10, 8, 8)
for axi, center in zip(ax.flat, centers):
   axi.set(xticks=[], yticks=[])
   axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)
fig.show()
wait =  input("Wait here: ")
"""
Output
As output, we will get following image showing clusters centers learned by k-means.

Visualizing Digits Clusters Centers
The following lines of code will match the learned cluster labels with the true labels found in them −
"""
from scipy.stats import mode
labels = np.zeros_like(clusters)
for i in range(10):
   mask = (clusters == i)
   labels[mask] = mode(digits.target[mask])[0]

"""
Next, we can check the accuracy as follows −
"""
from sklearn.metrics import accuracy_score

print("accuracy_score:" , accuracy_score(digits.target, labels))

"""
Output
0.7935447968836951
"""