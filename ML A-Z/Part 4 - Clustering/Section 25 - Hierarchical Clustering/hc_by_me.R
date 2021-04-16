# Hierarchical Clustering

# Importing the mall dataset
dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]

# Using de dendrogram to find the optima number of clusters
dendrogram = hclust(dist(X, method = 'euclidian'), method = 'ward.D')
plot(dendrogram,
     main = paste('Dendrogram'),
     xlab = 'Customers',
     ylab = 'Euclidian distances')

# Fitting hierachical clustering to the mall dataset
hc = hclust(dist(X, method = 'euclidian'), method = 'ward.D')
y_hc = cutree(hc, 5)

# Visualing the clusters
library(cluster)
clusplot(X,
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('Clusters of customers'),
         xlab = 'Annual Income',
         ylab = 'Spending Score')