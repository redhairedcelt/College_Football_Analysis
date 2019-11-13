# Analysis of College Football Games, 1950 to 2019

Welcome!  This is my analysis of all college football games played from 1950 to 2018, with particular focus on how accurate the Associated Press polls are at predicting the "best" team.  I also explore some basic community detection approaches to see if I can identify what conference a team plays in solely based on what teams they play.

This work is broken into three notebooks.  
* The [first notebook](https://redhairedcelt.github.io/college_football_analysis/CF_Scrape.html) includes the web scraper.  
* The [second notebook](https://redhairedcelt.github.io/college_football_analysis/CF_Analysis.html) has the bulk of the analysis.  
* The [third notebook](https://redhairedcelt.github.io/college_football_analysis/CF_Network_Analysis.html) includes my initial foray into network analysis.

## Key Findings
* The number of games played each year has varied dramatically over the last 70 years.
* The AP poll usually picks the correct winner when two ranked teams play each other.
* The polls are less accurate at the end of the season, possible because teams are more evenly matched in the conference championships and bowl games.
* When higher ranked teams beat lower ranked teams, they usually do so by much larger point margins.
* The 1960's were a tough time for poll accuracy.
* After some data cleaning, we can successfully identify conference structures by looking at the different teams each team plays, which form communities.  

## Conclusions
This analysis has shown that most of the time, the AP polls are pretty accurate.  Games at the end of the year are usually between more closely matched team, which makes it more difficult for pollsters to pick the best team.  Interestingly, the polls are about as good in the beginning of the year as they are through about week 13, suggesting the pollsters are just as accurate in pre-season polls and early polls when they only have seen a few games from each team.  The most positive rank difference in a week is week 14, with a score close to +4.  This week usually is the last week of the regular season and usually includes major rivalry games, suggesting pollsters are well-positioned to predict the winner of these games in the future.

Additionally, the network analysis shows the power of community detection to identify unseen relationships between nodes that interact with other nodes.  Not only can it be used to find relationships between different football teams, but hopefully to find other, non-obvious ways that different entities relate in dense datasets.

## Additional Ideas
There are multiple different directions this work could go in.  I would be interested in determining teams that are consistently over or under ranked by looking at their accumulated rank difference when they were the winner or losers, but we can save that for a different project.  There is also an oppertunity to see how rankings average across conferences to see if different conferences are over or under ranked.  Using network analysis, we could also try to find the most intense rivalries between different teams.  

