import numpy as np
import matplotlib.pyplot as plt
import random

# Sample Data: Each row is a data point (x, y)
data = np.array([
    [1.0, 2.0], [1.5, 1.8], [5.0, 8.0],
    [8.0, 8.0], [1.0, 0.6], [9.0, 11.0],
    [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]
])

# Number of clusters
k = 3

# Initialize centroids randomly
centroids = data[random.sample(range(len(data)), k)]

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# Repeat until convergence or max iterations
max_iterations = 100
for _ in range(max_iterations):
    # Step 1: Assign clusters
    clusters = [[] for _ in range(k)]
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        cluster_index = np.argmin(distances)
        clusters[cluster_index].append(point)
    
    # Step 2: Update centroids
    new_centroids = []
    for cluster in clusters:
        if cluster:
            new_centroids.append(np.mean(cluster, axis=0))
        else:
            # Handle empty cluster by reinitializing randomly
            new_centroids.append(data[random.randint(0, len(data) - 1)])
    
    new_centroids = np.array(new_centroids)
    
    # Check for convergence
    if np.allclose(centroids, new_centroids):
        break
    centroids = new_centroids

# Convert cluster lists to arrays for visualization
clusters = [np.array(cluster) for cluster in clusters]

# Visualization
colors = ['r', 'g', 'b']
for i in range(k):
    plt.scatter(clusters[i][:, 0], clusters[i][:, 1], c=colors[i], label=f'Cluster {i+1}')
    plt.scatter(centroids[i][0], centroids[i][1], c='black', marker='x', s=100)

plt.title('K-Means Clustering without Sklearn')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
