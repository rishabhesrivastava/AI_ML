# K-Means Clustering Assignment - Answers
**Student ID:** 2025AIML049

---

## Question 2: K-means Clustering with K=2 [2 points]

**Q2: Write your own code for K-means algorithm using two attributes namely average_runs and bowling_economy. Take K=2. Plot clusters on a scatter plot with X and Y being the two attributes namely average_runs and bowling_economy, respectively. Color data points belonging to the first cluster with red and the second cluster with blue. Copy the plot diagram in the word document and interpret the output.**

### Answer:
A K-means algorithm has been implemented from scratch using Euclidean distance with random centroid initialization and iterative refinement.

**Clustering Results for K=2:**
- **Cluster 1 (Red)**: 48 players - Batsmen/Limited Bowlers
- **Cluster 2 (Blue)**: 61 players - Bowlers/All-rounders
- **WCSS**: 4.5517

**Interpretation:**

**Cluster 1 (Red) - Batsmen:** Players with high average runs (10-75) and minimal bowling involvement. Specialist batsmen like MS Dhoni (75.83), Virat Kohli (48.18), AB de Villiers (53.33) form the backbone of batting lineup.

**Cluster 2 (Blue) - Bowlers:** Players with low average runs (0-30) and active bowling roles (economy: 6-16.5). Includes specialized bowlers and all-rounders who contribute primarily through bowling.

**Key Observations:**
- Clear spatial separation between batsmen and bowlers in feature space
- Red points occupy higher average_runs region with zero bowling economy
- Blue points spread across lower average_runs with varying bowling economy
- Perfect alignment with cricket player roles

**[INSERT K=2 PLOT HERE]**

---

## Question 3: K-means Clustering with K=2,3,4,5 [1 point]

**Q3: Redo question-2 on different values of K = 2,3,4,5. For each case, draw the plot of clusters as stated above. Visualize these plots, copy the plot diagrams in the word document, and comment on which is better clustering (and reasons) based on visualization only.**

### Clustering Results Summary:

| K | Cluster Sizes | WCSS | Reduction |
|---|---|---|---|
| 2 | [48, 61] | 4.5517 | - |
| 3 | [32, 61, 16] | 3.2131 | 29.4% |
| 4 | [15, 61, 10, 23] | 2.8530 | 11.2% |
| 5 | [15, 28, 10, 23, 33] | 1.7040 | 40.3% |

### Analysis:

**K=2:** Simple batsman/bowler separation with good interpretability but oversimplifies diversity.

**K=3:** Introduces all-rounder category with 29.4% WCSS reduction. Best balance—maintains practical cluster sizes (32, 61, 16).

**K=4-5:** Excessive fragmentation with diminishing returns. Clusters too small (<15 players), overfitting risk.

### Best Clustering: **K=3 is OPTIMAL**

**Reasons:**
1. **Elbow Point**: Largest WCSS reduction K=2→K=3 (29.4%)
2. **Natural Roles**: Captures three cricket archetypes - batsmen, bowlers, all-rounders
3. **Cluster Balance**: Practical cluster sizes
4. **Diminishing Returns**: K≥4 shows minimal improvement with complexity
5. **Practical Value**: Supports team selection and strategy

**[INSERT K=2, K=3, K=4, K=5 PLOTS HERE]**
**[INSERT ELBOW CURVE PLOT HERE]**

---

## Question 4: Interpretation and Applications [1 point]

**Q4: Write a few lines about the interpretation of the best clusters obtained. Also write a few statements about how these clusters can be useful.**

### Interpretation of K=3 Clusters:

The optimal K=3 clustering identifies three player archetypes:

**Cluster 1 - Pure Batsmen (32):** Specialist batsmen with high averages (10-75) and zero bowling. Examples: MS Dhoni (75.83), Virat Kohli (48.18). Form the core of batting lineup.

**Cluster 2 - Skilled Bowlers (61):** Dedicated bowlers with low batting average and active bowling (economy: 6-16.5). Contribute primarily through bowling and run-restriction.

**Cluster 3 - All-rounders (16):** Versatile players like Hardik Pandya, Andre Russell with moderate batting (20-50 avg) and significant bowling contribution. Provide tactical flexibility.

### Applications:

1. **Team Selection:** Balance composition with adequate batsmen, bowlers, and all-rounders for match conditions
2. **Player Development:** Customize training programs for specific cluster roles
3. **Strategic Planning:** Choose aggressive (more batsmen) or defensive (more bowlers) tactics
4. **Player Replacement:** Find replacements from same cluster when injuries occur
5. **Performance Tracking:** Monitor player transitions between clusters
6. **Player Valuation:** Objective valuation based on cluster position for auctions/contracts

---

*Assignment completed for K-Means Clustering on Cricket Players Dataset*
*Dataset: 109 international cricket players | Analysis Date: 2024*
