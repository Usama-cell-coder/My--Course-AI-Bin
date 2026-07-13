"""
https://www.geeksforgeeks.org/machine-learning/hierarchical-clustering/

Computing Distance Matrix
While merging two clusters we check the distance between two every pair of clusters and merge the pair with the least distance/most similarity. But the question is how is that distance determined. There are different ways of defining Inter Cluster distance/similarity. Some of them are:

Min Distance: Find the minimum distance between any two points of the cluster.
Max Distance: Find the maximum distance between any two points of the cluster.
Group Average: Find the average distance between every two points of the clusters.
Ward's Method: The similarity of two clusters is based on the increase in squared error when two clusters are merged.

"""

import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt


X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

Z = linkage(X, 'ward') # Ward Distance

dendrogram(Z) #plotting the dendogram

plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data point')
plt.ylabel('Distance')
plt.show()