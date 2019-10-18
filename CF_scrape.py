#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

import json #for parsing the return from the Google API
import urllib #for passing info to the Google API
import requests
from bs4 import BeautifulSoup


# In[4]:





# In[5]:


website = 'https://www.sports-reference.com/cfb/years/{}-schedule.html'.format(year)
year = 2017
response = requests.get(website)
soup = BeautifulSoup(response.text, 'html.parser')

# In[42]:





# In[41]:


response


# In[46]:



print(soup.prettify())

# In[45]:


table = soup.find_all('table')
print(len(table[0].text))

# In[29]:

for item in table[0].find_all('tr')[12]:
    print(item)
    print ()
    print('*************')

# In[ ]:
table[0].find_all('td')
table[0].find_all('tr')[-1]
#%%

def bs_to_list(bs):
    text_list = []
    for item in bs:
        text_list.append(item.text)
    return text_list

#%%
df = pd.DataFrame()
for year in range (1950,2019,1):
    print(year, 'starting now...')
    # make a dataframe to hold all the data

    # set the website we scarpe from using the year variable
    website = 'https://www.sports-reference.com/cfb/years/{}-schedule.html'.format(year)
    # get the response, parse it with bs4, and find the table tags
    response = requests.get(website)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table')
    
    # for all the desired data, find the associate data-stat tags
    row =  table[0].find_all('th', {'scope':'row'})
    week_number = table[0].find_all('td', {'data-stat':'week_number'})
    date_game = table[0].find_all('td', {'data-stat':'date_game'})
    time_game = table[0].find_all('td', {'data-stat':'time_game'})
    day_game =  table[0].find_all('td', {'data-stat':'day_name'})
    winner = table[0].find_all('td', {'data-stat':'winner_school_name'})
    winner_pts  = table[0].find_all('td', {'data-stat':'winner_points'})
    game_location = table[0].find_all('td', {'data-stat':'game_location'})
    loser = table[0].find_all('td', {'data-stat':'loser_school_name'})
    loser_pts = table[0].find_all('td', {'data-stat':'loser_points'})
    notes = table[0].find_all('td', {'data-stat':'notes'})
    
    # iterate through the bs4
    row_list = bs_to_list(row)
    week_number_list = bs_to_list(week_number)
    date_list = bs_to_list(date_game)
    time_list = bs_to_list(time_game)
    day_list = bs_to_list(day_game)
    winner_list = bs_to_list(winner)
    winner_pts_list = bs_to_list(winner_pts)
    game_loc_list = bs_to_list(game_location)
    loser_list = bs_to_list(loser)
    loser_pts_list = bs_to_list(loser_pts)
    notes_list = bs_to_list(notes)
    
    df_temp = pd.DataFrame(zip(row_list, week_number_list, date_list, time_list,
                      day_list, winner_list, winner_pts_list, game_loc_list,
                      loser_list, loser_pts_list, notes_list), columns = 
                    ['row','week','date_game','time_game','day_game','winner',
                     'winner_pts','game_loc','loser','loser_pts','notes'])
    df_temp['year'] = year
    df = df.append(df_temp)
    print(year, 'complete!')
    time.sleep(3)


#%%
df.to_csv('scraped_results_df.csv')
#%%
df.describe()




