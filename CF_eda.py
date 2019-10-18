#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[47]:


cf_2018 = pd.read_csv('2018.csv')
cf_2018.head()


# After exploring the data, we can reimport it and make the following changes to clean it up and provide additional, relevant information we will need for our EDA.

# In[48]:


# Read in the file again.
cf_2018 = pd.read_csv('2018.csv')

# 'Unnamed: 7' indicated where the game was played at. Since the winner is listed first, the '@' indicates
# the game was played at the loser's home.  Therefore, we can create a new column called 'Winner_home' if 
# the '@' sign is not present.
cf_2018['Winner_home'] = cf_2018['Unnamed: 7']!='@'

# The rank is included in the winner and losers name within parenthesis.  The below regex will identify 
# numerical digits within the parenthesis and extract them to a new column as 'floats'.  We'll also 
# remove the rank in parenthesis from the original winner column.  We'll do this for winners and losers.
cf_2018['Winner_rank'] = cf_2018['Winner'].str.extract('\(([0-9]+)\)', expand=True).astype('float')
cf_2018['Winner'] = cf_2018['Winner'].str.replace('\(([0-9]+)\)', '').str.replace('\xa0', '')
cf_2018['Loser_rank'] = cf_2018['Loser'].str.extract('\(([0-9]+)\)', expand=True).astype('float')
cf_2018['Loser'] = cf_2018['Loser'].str.replace('\(([0-9]+)\)', '').str.replace('\xa0', '')

# Calculate a rank_diff socre.  The more negative this is, the more of an upset it is.
cf_2018['Rank_diff'] = cf_2018['Loser_rank'] - cf_2018['Winner_rank']

# 'Pts' and 'Pts.1' are unclear.  Lets make it a bit more obvious and also calculate the helpful difference
# between the two values as we can use margin of victory to see how close a game is.
cf_2018['Winner_pts'] = cf_2018['Pts']
cf_2018['Loser_pts'] = cf_2018['Pts.1']
cf_2018['Pts_diff'] = cf_2018['Winner_pts'] - cf_2018['Loser_pts']

# We no longer need several of these columns, so lets drop them.  We can keep the time fields in case
# we need them for later analysis.
cf_2018.drop(['Unnamed: 7', 'Pts', 'Pts.1', 'TV', 'Notes', 'Rk'], axis=1, inplace=True)

# Theres some weird formatting in the first line, and it didnt get dropped earlier.  Let's manually drop it
# and reindex the dataframe.
cf_2018.drop(0, axis=0, inplace=True)
cf_2018.reset_index(inplace=True, drop=True)


# In[49]:


cf_2018.head()


# In[50]:


cf_2018.tail()


# In[51]:


cf_2018.info()


# In[52]:


cf_2018.describe()


# In[53]:


cf_2018[['Winner_pts', 'Loser_pts', 'Pts_diff', 'Rank_diff']].hist(figsize=(12,6))


# In[54]:


cf_2018[['Winner_pts', 'Loser_pts', 'Pts_diff', 'Rank_diff']].boxplot(figsize=(12,6))


# ## Lets look at when ranked teams play other ranked teams.

# Lets look at when ranked team play each other.  From 'Rank_diff', there should be 58 such games in 2018.  Turns out the polls were right 37 out of 58 times, for a success rate of .638.  We could look at the likelihood that this is chance.

# In[55]:


higher_beats_lower = cf_2018[cf_2018['Winner_rank'] < cf_2018['Loser_rank']]
print('Number of times a higher ranked team beats a lower ranked team:', len(higher_beats_lower))

lower_beats_higher = cf_2018[cf_2018['Winner_rank'] > cf_2018['Loser_rank']]
print('Number of times a lower ranked team beats a higher ranked team:', len(lower_beats_higher))


# It also seems that the games are closer in score when the lower ranked team beats the favored team.  The average points difference when a higher team beat a lower team was 16.03, but it was only 12.90 when the lower ranked team won.  It also seemed that a higher percentage of games was won by less than 10 points (what we could call a "close" game) when the lower ranked team won.
# 
# Also, the absolute value of the rank_diff score is higher in the subset of data when higer teams defeat lower-ranked teams as expected.  There, the average rank_dff is 9.05.  When a lower-ranked team upsets a higher ranked team, the rank_diff is 6.81.  This suggests that polls are less accurate when the ranks between teams are less.  This makes sense because pollsters would be more likely to guess the winner when the #1 team played the #25 team than when the #12 team plays the #13 team.

# In[56]:


higher_beats_lower.describe()


# In[57]:


higher_beats_lower['Pts_diff'].hist()


# In[58]:


lower_beats_higher.describe()


# In[59]:


lower_beats_higher['Pts_diff'].hist()


# ## Lets look at ranked teams vs unranked teams

# First, lets find out how many games there should be with at least one ranked team.  There are 884 games, so the total numers of games with at least one ranked and no one ranked should be 884.

# In[60]:


at_least_one_ranked = cf_2018[(cf_2018['Winner_rank'] > 0) | (cf_2018['Loser_rank'] > 0)]
print('Numbers of games where at least one team is ranked:', len(at_least_one_ranked))

no_ranked = cf_2018[(cf_2018['Winner_rank'].isna()) & (cf_2018['Loser_rank'].isna())]
print('Numbers of games where no team is ranked:', len(no_ranked))


# Looks good!  Now lets look closer at the games when only one team is ranked.  We'll break that out to two dataframes, when the ranked team wins and when the unranked team wins.

# In[61]:


ranked_beats_unranked = cf_2018[(cf_2018['Winner_rank'] > 0) & (cf_2018['Loser_rank'].isna())]
print('Number of times a ranked team beats an unranked team:', len(ranked_beats_unranked))

unranked_beats_ranked = cf_2018[(cf_2018['Winner_rank'].isna()) & (cf_2018['Loser_rank'] > 0)]
print('Number of times an unranked team upsets a ranked team:', len(unranked_beats_ranked))


# These values add to 223, which with the 58 games examined above included adds up to 281, the total number of games with at least one ranked team.  So we are inclusive with all of our conditions.

# ## Team Exploration

# In[66]:


winner_team = cf_2018['Winner'].unique().tolist()
loser_team = cf_2018['Loser'].unique().tolist()
teams = set(winner_team + loser_team)


# In[69]:


len(teams)


# In[71]:


cf_2018['Loser'].value_counts()


# In[ ]:


cf_2018['Loser'].value_counts()


# In[ ]:




