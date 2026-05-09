Dataset Schema
Column	Description
country	Name of the country.
child_mort	Under-5 mortality rate: deaths of children under 5 per 1,000 live births.
exports	Exports of goods and services per capita, expressed as a percentage of GDP per capita.
health	Total health spending per capita, expressed as a percentage of GDP per capita.
imports	Imports of goods and services per capita, expressed as a percentage of GDP per capita.
income	Net income per person.
inflation	Annual growth rate of total GDP (inflation rate).
life_expec	Life expectancy: average number of years a newborn would live if current mortality patterns hold.
total_fer	Total fertility rate: number of children a woman would bear if current age-specific fertility rates persist.
gdpp	GDP per capita: total GDP divided by total population.
Tasks & Rubric
Complete all tasks in a single Jupyter notebook with inline outputs.

Task	Marks
a) Developed vs. Developing Identification
• Define Developed Countries as those with both gdpp and life_expec above their respective medians.
• List these countries and similarly list Developing Countries where both metrics fall below the medians.	3
b) K-Means Clustering
• Apply K-means clustering for K=2,3,4,5K = 2,3,4,5K=2,3,4,5 using scikit-learn’s KMeansScikit-learn.
• Compute the mean Silhouette score for each KKK using silhouette_scoreScikit-learn.	3
c) Cluster Visualization
• Reduce to 2 dimensions via PCA (sklearn.decomposition.PCA) Scikit-learnGeeksforGeeks.
• For each KKK, plot clusters in 2-D with distinct colors.
• Annotate 5 sample countries per cluster by name.	3
d) Silhouette Plot
• Draw a bar chart of Silhouette score vs. KKK to illustrate cluster cohesion vs. separation Scikit-learn.	1.5
e) Cluster Interpretation
• Provide 5 representative countries per cluster.
• Assign each cluster an intuitive label (e.g., “High-Income Developed”, “High Mortality Aid-Needed”) Scikit-learn.	1.5
References:

K-Means: KMeans — scikit-learn 1.6.1 documentation)

Silhouette Score: silhouette_score — scikit-learn 1.6.1 documentation, Selecting the number of clusters with silhouette ... - scikit-learn

PCA: PCA — scikit-learn 1.6.1 documentation

Submission Guidelines
Submit one Jupyter notebook (.ipynb) with all code executed and outputs inline.

Do not submit zip files.

Ensure the notebook is the final version: all results visible, formatting clear.

Late submissions incur –2 marks/day.

Plagiarism checks will be performed; any infractions yield zero marks.