#!/usr/bin/env python
# coding: utf-8

# In[25]:
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup
import unittest

# %% Unit Tests

class SimpleTest(unittest.TestCase):
   def test1(self):
      self.assertEqual(ranker_last_element, len(data_list), test_1_msg)

#%% Function (one massive function...)

def scrape_and_process_sports_ref(stat, start_year, end_year):
    # make a dataframe to hold all the data
    df = pd.DataFrame()
    for year in range (start_year, end_year, 1):
        print(year, 'starting now...')
        # use requests to scrape the website, and bs4 to parse the response
        try:
            website =  'https://www.sports-reference.com/cfb/years/{}-{}.html'.format(year, stat)
            response = requests.get(website)
            soup = BeautifulSoup(response.text, 'html.parser')
            # find the table tag, which contains all the data we are looking for
            table = soup.find_all('table')
        except:
            print('Failed to get site at: ', website)
            return df
            break
        
        # table's top level tag is 'tr', which has two rows of header data and many
        # repeated instances of the same headers throughout the data.
        table_data = (table[0].find_all('tr'))
        data_list = []
        for row in table_data:
            row_dict = {}
            try:
                for element in row:
                    row_dict[element.attrs['data-stat']] = (element.text)
                data_list.append(row_dict)
        
            # many rows have header data that we can skip.  we will ensure we didnt
            # skip anything valuable in the unit test.
            except: 
                continue
             
        df_temp = pd.DataFrame(data_list)
        df_temp['year'] = year
        df = df.append(df_temp)
        print(year, 'complete!')
        time.sleep(3)
        
        # we can check that we got all the row of data by ensuring that the length of
        # data_list is equal to the field 'ranker' of the last element
        
        test_1_msg = "Length of data_list does not equal 'ranker' of last element."
        ranker_last_element = int(data_list[-1]['ranker'])
        if __name__ == '__main__':
           unittest.main()
        
    return df


#%% Run function
        
offense_results = scrape_and_process_sports_ref('team-offense', 2017, 2019)
#offense_results.to_csv('offense_results.csv')
#%%

defense_results = scrape_and_process_sports_ref('team-defense', 2000, 2019)
defense_results.to_csv('defense_results.csv')
#%%

special_results = scrape_and_process_sports_ref('special-teams', 2000, 2019)
special_results.to_csv('special_results.csv')
#%%
standings_results = scrape_and_process_sports_ref('standings', 2000, 2019)
standings_results.to_csv('standings_results.csv')


#%% Attempt to break out function to two smaller functions.  Needs more work.
def scrape_sports_ref(year, stat):
    # make a dataframe to hold all the data
        try:
            website =  'https://www.sports-reference.com/cfb/years/{}-{}.html'.format(year, stat)
            response = requests.get(website)
            soup = BeautifulSoup(response.text, 'html.parser')
            # find the table tag, which contains all the data we are looking for
            table = soup.find_all('table')
            # table's top level tag is 'tr', which has two rows of header data and many
            # repeated instances of the same headers throughout the data.
            return table[0].find_all('tr')
        except:
            print('Failed to get site at: ', website)
     
# %%
def parse_results(start_year, end_year, stat):
    # make a dataframe to hold all the data
    df = pd.DataFrame()
    for year in range (start_year, end_year, 1):
        print(year, 'starting now...')
        # use earlier defined function
        table_data = scrape_sports_ref(year, stat)    
        
        data_list = []
        for row in table_data:
            row_dict = {}
            try:
                for element in row:
                    row_dict[element.attrs['data-stat']] = (element.text)
                data_list.append(row_dict)
        
            # many rows have header data that we can skip.  we will ensure we didnt
            # skip anything valuable in the unit test.
            except: 
                continue
             
        df_temp = pd.DataFrame(data_list)
        df_temp['year'] = year
        df = df.append(df_temp)
        print(year, 'complete!')
        time.sleep(3)
# %%
scrape_result = parse_results(2000, 2005, 'team-offense')