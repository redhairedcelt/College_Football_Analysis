```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date

import json #for parsing the return from the Google API
import urllib #for passing info to the Google API
import requests
from bs4 import BeautifulSoup
```

To gather the data, we will scrape the below website.  The site has an embedded table for each year including all the games played in that year.  They also include the Associated Press poll ranking for each team for every game.  1950 is the first year where the AP poll ranked teams in the pre-season, giving teams ranks for their first games.

The goal here is to find the embedded table, extract it, save all the features as columns in a Pandas dataframe, combine all years, and save the final dataframe as a csv.


```python
# test accessing the website
year = 2017
website = 'https://www.sports-reference.com/cfb/years/{}-schedule.html'.format(year)

response = requests.get(website)
soup = BeautifulSoup(response.text, 'html.parser')
print(response)
```

    <Response [200]>



```python
print(soup.prettify()[:1000])
```

    <!DOCTYPE html>
    <html class="no-js" data-root="/home/cfb/build" data-version="klecko-" itemscope="" itemtype="https://schema.org/WebSite" lang="en">
     <head>
      <meta charset="utf-8"/>
      <meta content="ie=edge" http-equiv="x-ua-compatible"/>
      <meta content="width=device-width, initial-scale=1.0, maximum-scale=2.0" name="viewport">
       <link href="https://d2p3bygnnzw9w3.cloudfront.net/req/201910231" rel="dns-prefetch"/>
       <!-- no:cookie fast load the css.           -->
       <script>
        function gup(n) {n = n.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]'); var r = new RegExp('[\\?&]'+n+'=([^&#]*)'); var re = r.exec(location.search);   return re === null?'':decodeURIComponent(re[1].replace(/\+/g,' '));}; document.srdev = gup('srdev')
       </script>
       <link crossorigin="" href="https://d2p3bygnnzw9w3.cloudfront.net" rel="preconnect"/>
       <link crossorigin="" href="https://d17lgqwvsissft.cloudfront.net" rel="preconnect"/>
       <style>
        html,body{margin:0;padding:0;font:14px/1.25 "Helvetica Neu



```python
table = soup.find_all('table')
print(len(table[0].text))
print()
print((table[0].text)[:500])
```

    85166
    
    874 Games Table
    
    
    
    Rk
    Wk
    Date
    Time
    Day
    Winner
    Pts
    
    Loser
    Pts
    Notes
    
    
    
    11Aug 26, 20173:00 PMSatBrigham Young20Portland State6LaVell Edwards Stadium - Provo, Utah
    21Aug 26, 20172:30 PMSatColorado State58Oregon State27Sonny Lubrick Field at Colorado State Stadium - Fort Collins, Colorado
    31Aug 26, 20176:00 PMSatHawaii38@Massachusetts35Warren McGuirk Alumni Stadium - Amherst, Massachusetts
    41Aug 26, 20177:30 PMSat(19) South Florida42@San Jose State22CEFCU Stadium - San Jose, California
    51Aug 26, 201



```python
# We will use this function in the larger function below to parse beautiful soup to lists.
# This function has the added advantage of assigning None if the field does not exist, which
# happens in earlier years of the data.
def bs_to_list(bs):
    text_list = []
    if len (bs) > 0 :
        for item in bs:
            text_list.append(item.text)
        return text_list
    else:
        return None
```


```python
# make a dataframe to hold all the data.  create df outside of loop.
df = pd.DataFrame()
for year in range (1950,2019,1):
    print(year, 'starting now...')

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
    
    # make an empty temp df and add each row as a columns.
    # this was neccessary to assign "None" to any fields that did not
    # exist in earlier years
    df_temp = pd.DataFrame()
    
    # iterate through the bs4
    df_temp['row'] = bs_to_list(row)
    df_temp['week_number'] = bs_to_list(week_number)
    df_temp['winner'] = bs_to_list(winner)
    df_temp['winner_pts'] = bs_to_list(winner_pts)
    df_temp['loser'] = bs_to_list(loser)
    df_temp['loser_pts'] = bs_to_list(loser_pts)
    df_temp['game_date'] = bs_to_list(date_game)
    df_temp['game_time'] = bs_to_list(time_game)
    df_temp['game_day'] = bs_to_list(day_game)
    df_temp['game_loc'] = bs_to_list(game_location)
    df_temp['notes'] = bs_to_list(notes)
    
    # assign a new column for each df_temp with the year
    df_temp['year'] = year
    # append the newly generated df_temp to the full df
    df = df.append(df_temp)
    print(year, 'complete!')
    # stop the scraper for a second to prevent overwhelming the website.
    # the terms of use for the site requested scraping no faster than a human 
    # could access the data and I figured this was a good time interval.
    time.sleep(5)
```

    1950 starting now...
    1950 complete!
    1951 starting now...
    1951 complete!
    1952 starting now...
    1952 complete!
    1953 starting now...
    1953 complete!
    1954 starting now...
    1954 complete!
    1955 starting now...
    1955 complete!
    1956 starting now...
    1956 complete!
    1957 starting now...
    1957 complete!
    1958 starting now...
    1958 complete!
    1959 starting now...
    1959 complete!
    1960 starting now...
    1960 complete!
    1961 starting now...
    1961 complete!
    1962 starting now...
    1962 complete!
    1963 starting now...
    1963 complete!
    1964 starting now...
    1964 complete!
    1965 starting now...
    1965 complete!
    1966 starting now...
    1966 complete!
    1967 starting now...
    1967 complete!
    1968 starting now...
    1968 complete!
    1969 starting now...
    1969 complete!
    1970 starting now...
    1970 complete!
    1971 starting now...
    1971 complete!
    1972 starting now...
    1972 complete!
    1973 starting now...
    1973 complete!
    1974 starting now...
    1974 complete!
    1975 starting now...
    1975 complete!
    1976 starting now...
    1976 complete!
    1977 starting now...
    1977 complete!
    1978 starting now...
    1978 complete!
    1979 starting now...
    1979 complete!
    1980 starting now...
    1980 complete!
    1981 starting now...
    1981 complete!
    1982 starting now...
    1982 complete!
    1983 starting now...
    1983 complete!
    1984 starting now...
    1984 complete!
    1985 starting now...
    1985 complete!
    1986 starting now...
    1986 complete!
    1987 starting now...
    1987 complete!
    1988 starting now...
    1988 complete!
    1989 starting now...
    1989 complete!
    1990 starting now...
    1990 complete!
    1991 starting now...
    1991 complete!
    1992 starting now...
    1992 complete!
    1993 starting now...
    1993 complete!
    1994 starting now...
    1994 complete!
    1995 starting now...
    1995 complete!
    1996 starting now...
    1996 complete!
    1997 starting now...
    1997 complete!
    1998 starting now...
    1998 complete!
    1999 starting now...
    1999 complete!
    2000 starting now...
    2000 complete!
    2001 starting now...
    2001 complete!
    2002 starting now...
    2002 complete!
    2003 starting now...
    2003 complete!
    2004 starting now...
    2004 complete!
    2005 starting now...
    2005 complete!
    2006 starting now...
    2006 complete!
    2007 starting now...
    2007 complete!
    2008 starting now...
    2008 complete!
    2009 starting now...
    2009 complete!
    2010 starting now...
    2010 complete!
    2011 starting now...
    2011 complete!
    2012 starting now...
    2012 complete!
    2013 starting now...
    2013 complete!
    2014 starting now...
    2014 complete!
    2015 starting now...
    2015 complete!
    2016 starting now...
    2016 complete!
    2017 starting now...
    2017 complete!
    2018 starting now...
    2018 complete!



```python
# Save the final file as a csv.  Append todays date to the filename
# to keep for overwriting the full file and to document when the site
# was scraped.
today = str(date.today())
df.to_csv('scraped_results/{}.csv'.format(today))
```
