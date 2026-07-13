""""
https://www.geeksforgeeks.org/machine-learning/hierarchical-clustering/


Hierarchical Agglomerative Clustering
It is also known as the bottom-up approach or hierarchical agglomerative clustering (HAC). Unlike flat clustering 
hierarchical clustering provides a structured way to group data. This clustering algorithm does not require us to 
prespecify the number of clusters. Bottom-up algorithms treat each data as a singleton cluster at the outset and then
 successively agglomerate pairs of clusters until all clusters have been merged into a single cluster that contains 
 all data. 

Workflow for Hierarchical Agglomerative clustering
Start with individual points: Each data point is its own cluster. For example if you have 5 data points you start with 5 clusters each containing just one data point.
Calculate distances between clusters: Calculate the distance between every pair of clusters. Initially since each cluster has one point this is the distance between the two data points.
Merge the closest clusters: Identify the two clusters with the smallest distance and merge them into a single cluster.
Update distance matrix: After merging you now have one less cluster. Recalculate the distances between the new cluster and the remaining clusters.
Repeat steps 3 and 4: Keep merging the closest clusters and updating the distance matrix until you have only one cluster left.
Create a dendrogram: As the process continues you can visualize the merging of clusters using a tree-like diagram called a dendrogram. It shows the hierarchy of how clusters are merged.
"""
from sklearn.cluster import AgglomerativeClustering
import numpy as np

X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])


clustering = AgglomerativeClustering(n_clusters=2).fit(X)

print(clustering.labels_)
"""
Output : 

[1, 1, 1, 0, 0, 0]
"""