Market segmentation allows insurance providers to identify different customer groups with similar traits and behaviors. This enables personalized recommendations, targeted marketing campaigns, and efficient product offerings.

Objective

To perform customer segmentation using clustering algorithms and gain actionable insights 

Dataset

Dataset: https://taxila-aws.bits-pilani.ac.in/pluginfile.php/1612076/mod_assign/intro/Customer%20Data%202.csv
Records: ~9,000 customers
Task 1: Perform EDA and Preprocessing  [1 Mark]

Load and inspect the dataset (shape, columns, types)
Handle missing values, duplicates, outliers
Normalize or standardize numerical columns
Use visual tools (histograms, boxplots, pairplots, correlation heatmaps) to explore relationships
Task 2: Apply Clustering Algorithms  [2 Marks]

You will apply the following clustering algorithms:

a) Agglomerative Clustering

Try various linkage types: single, complete, average
Experiment with distance metrics: euclidean, manhattan, cosine
Visualize dendrograms to decide on optimal clusters
b) DBSCAN

Use k-distance plot to estimate the best eps
Vary min_samples to analyze impact on cluster formation
Identify noise points (outliers) in the dataset
c) K-Means Clustering [1 Mark]

Use Elbow method and Silhouette Score to determine the ideal number of clusters
Run K-means and visualize the results
Task 3: Compare Clustering Algorithms  [1 Mark]

Create a comparison table or bar chart for better visualization
Task 4: Interpret Clusters and Derive Insights [1 Mark]

Select the best clustering algorithm from the above step
Describe the characteristics of each cluster:
Provide actionable business recommendations for each segment:
 Expected Deliverables

Submit your work as a single Jupyter notebook & .html of the same which has all the outputs visible.     Do not submit zip files. Do not upload dataset.