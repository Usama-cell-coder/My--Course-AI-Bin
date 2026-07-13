"""
https://www.geeksforgeeks.org/machine-learning/k-means-clustering-introduction/

"""

"""import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

"""Step 2: Create custom dataset with make_blobs and plot it
"""

X,y = make_blobs(n_samples = 500,n_features = 2,centers = 3,random_state = 23)

fig = plt.figure(0)
plt.grid(True)
plt.scatter(X[:,0],X[:,1])
plt.show()


"""
Step 3: Initializing random centroids
The code initializes three clusters for K-means clustering. It sets a random seed and generates random cluster centers within a specified range and creates an empty list of points for each cluster.
"""

k = 3

clusters = {}
np.random.seed(23)

for idx in range(k):
    center = 2*(2*np.random.random((X.shape[1],))-1)
    points = []
    cluster = {
        'center' : center,
        'points' : []
    }
    
    clusters[idx] = cluster
    
clusters

"""
Step 4: Plotting random initialize center with data points
"""

plt.scatter(X[:,0],X[:,1])
plt.grid(True)
for i in clusters:
    center = clusters[i]['center']
    plt.scatter(center[0],center[1],marker = '*',c = 'red')
plt.show()

"""
Step 5: Defining Euclidean distance
"""

def distance(p1,p2):
    return np.sqrt(np.sum((p1-p2)**2))

"""
Step 6: Creating function Assign and Update the cluster center
This step assigns data points to the nearest cluster center and the M-step updates cluster centers based on the mean of assigned points in K-means clustering.
"""

def assign_clusters(X, clusters):
    for idx in range(X.shape[0]):
        dist = []
        
        curr_x = X[idx]
        
        for i in range(k):
            dis = distance(curr_x,clusters[i]['center'])
            dist.append(dis)
        curr_cluster = np.argmin(dist)
        clusters[curr_cluster]['points'].append(curr_x)
    return clusters

def update_clusters(X, clusters):
    for i in range(k):
        points = np.array(clusters[i]['points'])
        if points.shape[0] > 0:
            new_center = points.mean(axis =0)
            clusters[i]['center'] = new_center
            
            clusters[i]['points'] = []
    return clusters
"""
Step 7: Creating function to Predict the cluster for the datapoints
"""

def pred_cluster(X, clusters):
    pred = []
    for i in range(X.shape[0]):
        dist = []
        for j in range(k):
            dist.append(distance(X[i],clusters[j]['center']))
        pred.append(np.argmin(dist))
    return pred   
"""
Step 8: Assign, Update and predict the cluster center
"""
clusters = assign_clusters(X,clusters)
clusters = update_clusters(X,clusters)
pred = pred_cluster(X,clusters)

"""
Step 9: Plotting data points with their predicted cluster center
"""
plt.scatter(X[:,0],X[:,1],c = pred)
for i in clusters:
    center = clusters[i]['center']
    plt.scatter(center[0],center[1],marker = '^',c = 'red')
plt.show()