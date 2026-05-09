Consider the dataset comprising of 109 cricket players (attached here with assignment), filename is ‘cricketers.csv’. Each row comprises of following details of a cricketer: 

matches_played: number of matches played by the player, 
innings_batted: number of times got the chance to bat,
runs_scored: total runs scores across all innings,
highest_runs: highest run scored taking all innings in account,
ball_faced: total balls faced across all innings,
average_runs: average runs scores taking all innings in account, 
strike_rate: it is computed as (runs_scored / balls_faced) x 100,
innings_bowled: number of times got the chance to bowl,
overs: number of overs bowled across all innings,
runs_given: total run given across all innings,
wickets_obtained: total wickets obtained across all innings,
average_runs_per_wicket: it is computed as (runs_given / wickets_obtained)
bowling_economy: average runs scored per over
Questions:

Notes: Write all code related to this assignment in single jupyter notebook. Implement K-means algorithm from scratch, do not use any predefined ML library function for K-means algorithm. Use single word document to answer questions.

1. Given that K-means depends on distance metric, it is a convention to normalize the data attributes so that attributes are on the same scale.  So, in this first task, normalize all data attributes. [2 points]

2. Write your own code for K-means algorithm using two attributes namely average_runs and bowling_economy. Take K=2. Plot clusters on a scatter plot with X and Y being the two attributes namely average_runs and bowling_economy, respectively. Color data points belonging to the first cluster with red and the second cluster with blue. Copy the plot diagram in the word document and interpret the output. [2 points]

3. Redo question-2 on different values of K = 2,3,4,5. For each case, draw the plot of clusters as stated above. Visualize these plots, copy the plot diagrams in the word document,  and comment on which is better clustering (and reasons) based on visualization only. [1 points]

4. Write a few lines in a word document about the interpretation of the best clusters obtained. Also write a few statements about how these clusters can be useful. [1 points]

Deliverables:

One jupyter notebook for Q 1,2,3.

One word document for Q 2,3,4.

If you are not able to generate word file write answer in .md file with name answer.md and leave space for scatter plot I will copy all content in word manually.