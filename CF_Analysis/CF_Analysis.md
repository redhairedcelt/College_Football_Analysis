```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.graph_objects as go

%matplotlib inline
```


```python
sns.set(rc={'figure.figsize':(12, 6)})
```

We'll start our process by reading in the scarped results and conducting some data transformations and other changes to clean the date.


```python
records = pd.read_csv('scraped_results_df.csv')
```


```python
records.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 48899 entries, 0 to 48898
    Data columns (total 13 columns):
    Unnamed: 0     48899 non-null int64
    row            48899 non-null int64
    week_number    48899 non-null int64
    winner         48899 non-null object
    winner_pts     48897 non-null float64
    loser          48899 non-null object
    loser_pts      48897 non-null float64
    game_date      48899 non-null object
    game_time      5225 non-null object
    game_day       48899 non-null object
    game_loc       17923 non-null object
    notes          4066 non-null object
    year           48899 non-null int64
    dtypes: float64(2), int64(4), object(7)
    memory usage: 4.9+ MB



```python
records.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>row</th>
      <th>week_number</th>
      <th>winner_pts</th>
      <th>loser_pts</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>48899.000000</td>
      <td>48899.000000</td>
      <td>48899.000000</td>
      <td>48897.000000</td>
      <td>48897.000000</td>
      <td>48899.000000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>360.076361</td>
      <td>361.076361</td>
      <td>7.479539</td>
      <td>31.192159</td>
      <td>13.981389</td>
      <td>1985.805047</td>
    </tr>
    <tr>
      <td>std</td>
      <td>215.386657</td>
      <td>215.386657</td>
      <td>3.950671</td>
      <td>13.186025</td>
      <td>9.711082</td>
      <td>19.962510</td>
    </tr>
    <tr>
      <td>min</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1950.000000</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>177.000000</td>
      <td>178.000000</td>
      <td>4.000000</td>
      <td>21.000000</td>
      <td>7.000000</td>
      <td>1969.000000</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>354.000000</td>
      <td>355.000000</td>
      <td>7.000000</td>
      <td>30.000000</td>
      <td>13.000000</td>
      <td>1985.000000</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>531.000000</td>
      <td>532.000000</td>
      <td>10.000000</td>
      <td>40.000000</td>
      <td>20.000000</td>
      <td>2004.000000</td>
    </tr>
    <tr>
      <td>max</td>
      <td>883.000000</td>
      <td>884.000000</td>
      <td>21.000000</td>
      <td>100.000000</td>
      <td>72.000000</td>
      <td>2018.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
records.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>row</th>
      <th>week_number</th>
      <th>winner</th>
      <th>winner_pts</th>
      <th>loser</th>
      <th>loser_pts</th>
      <th>game_date</th>
      <th>game_time</th>
      <th>game_day</th>
      <th>game_loc</th>
      <th>notes</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>Presbyterian</td>
      <td>13.0</td>
      <td>Furman</td>
      <td>12.0</td>
      <td>Sep 15, 1950</td>
      <td>NaN</td>
      <td>Fri</td>
      <td>@</td>
      <td>NaN</td>
      <td>1950</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>Brigham Young</td>
      <td>14.0</td>
      <td>Idaho State</td>
      <td>13.0</td>
      <td>Sep 16, 1950</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>1950</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>Cincinnati</td>
      <td>32.0</td>
      <td>Texas-El Paso</td>
      <td>0.0</td>
      <td>Sep 16, 1950</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1950</td>
    </tr>
    <tr>
      <td>3</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>Citadel</td>
      <td>56.0</td>
      <td>Parris Island Marines</td>
      <td>0.0</td>
      <td>Sep 16, 1950</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1950</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>Drake</td>
      <td>7.0</td>
      <td>Denver</td>
      <td>0.0</td>
      <td>Sep 16, 1950</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1950</td>
    </tr>
  </tbody>
</table>
</div>




```python
records = pd.read_csv('scraped_results_df.csv')
# 'game_loc' indicated where the game was played at. Since the winner is listed first in 
# the original data, the '@' indicates the game was played at the loser's home.  Therefore, 
# we can create a new column called 'Winner_home' if the '@' sign is not present.
records['winner_home'] = records['game_loc']!='@'

# The rank is included in the winner and losers name within parenthesis.  The below regex will identify 
# numerical digits within the parenthesis and extract them to a new column as 'floats'.  We'll also 
# remove the rank in parenthesis from the original winner column.  We'll do this for winners and losers.
records['winner_rank'] = records['winner'].str.extract('\(([0-9]+)\)', expand=True).astype('float')
records['winner_name'] = records['winner'].str.replace('\(([0-9]+)\)', '').str.replace('\xa0', '')
records['loser_rank'] = records['loser'].str.extract('\(([0-9]+)\)', expand=True).astype('float')
records['loser_name'] = records['loser'].str.replace('\(([0-9]+)\)', '').str.replace('\xa0', '')

# Calculate a rank_diff socre.  The more negative this is, the more of an upset it is.
records['rank_diff'] = records['loser_rank'] - records['winner_rank']

# Add a pts_diff between the two pts as we can use margin of victory to see how close a 
# game is.
records['pts_diff'] = records['winner_pts'] - records['loser_pts']

# We no longer need several of these columns, so lets drop them.  
records.drop(['Unnamed: 0', 'winner','loser'], axis=1, inplace=True)

records.set_index(['year','week_number', 'row'], inplace=True)
```

## Inital Data Exploration

From the below plot, we can see a tremendous explosion in number of games in the 1970's.  In fact in 1977, the NCAA split into 1A for larger schools with better football teams and 1AA for smaller schools.  In recent years, part of the rise in number of games has been a proliferation of games played after the normal season, including bowl games and playoffs.


```python
ax = records.groupby('year').size().plot(figsize=(12,6), title='Games Played Per Year')
ax.set_xlabel('Year')
```




    Text(0.5, 0, 'Year')




![png](output_10_1.png)


By looking at the distribution of winner points, loser points, difference between points, and the rank difference over the entire data, several trends emerge.  First, winner points (the total number of points a winner scores) is mostly normally distributed.  On the other hand, the loser's points and the points difference are dramatically skewed to the right with most losers scoring less than 15 points and points differences less then 20.   


```python
records[['winner_pts', 'loser_pts', 'pts_diff', 'rank_diff']].hist(figsize=(12,6))

```




    array([[<matplotlib.axes._subplots.AxesSubplot object at 0x132cd7410>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x132c34950>],
           [<matplotlib.axes._subplots.AxesSubplot object at 0x132c6cc50>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x132f5a5d0>]],
          dtype=object)




![png](output_12_1.png)


By looking at points scored by the winners, losers, and the difference, we can see that over time more points have been scored by both teams.  However, the average points difference has remained relatively stead over the last 70 years.


```python
records.groupby('year').mean().plot(y=['winner_pts','loser_pts','pts_diff'])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1330192d0>




![png](output_14_1.png)


If we want to look at how "accurate" the polls have been when ranked teams play each other, we could look at the rank difference between the two teams.  We would expect a positive score as that means the higher ranked team defeated the lower ranked team.  The plot below shows the variability of the average rank difference score over the last 70 years. 


```python
records.groupby('year').mean().plot(y='rank_diff')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x133c5c1d0>




![png](output_16_1.png)


By plotting points difference against the rank difference, we see that the more positive the rank difference, the greater the margin of victory.  This makes sense when a higher ranked team plays and defeats a lower ranked team, the bigger difference in the rank leads to a more severe points difference.  However, this scatter plot does not work well with dense data like this.  Let's try using a hexplot from Seaborn.


```python
records.plot(x='rank_diff', y='pts_diff', kind='scatter', c='black')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x13300c590>




![png](output_18_1.png)



```python
sns.jointplot(x='rank_diff', y='pts_diff', data=records, kind='hex', height=8)
```




    <seaborn.axisgrid.JointGrid at 0x131503bd0>




![png](output_19_1.png)


This plot shows how many games are played in each week.  The small number of games played after week 12 relative to the rest of the year highlights both a longer season in recent years and the growth in "post-season" bowl games, conference champions, and most recently play-off games


```python
# total number of games per week
records.groupby('week_number').size().plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1330bce50>




![png](output_21_1.png)


Using the rank difference field, we can look for the biggest upsets between ranked teams.  A more negative rank difference indicates a more dramatic upset.  Next we can look at when unranked teams beat the number one ranked team.


```python
# Biggest upsets between ranked teams
records[records['rank_diff'] < -18].sort_values('rank_diff')[:5]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>winner_pts</th>
      <th>loser_pts</th>
      <th>game_date</th>
      <th>game_time</th>
      <th>game_day</th>
      <th>game_loc</th>
      <th>notes</th>
      <th>winner_home</th>
      <th>winner_rank</th>
      <th>winner_name</th>
      <th>loser_rank</th>
      <th>loser_name</th>
      <th>rank_diff</th>
      <th>pts_diff</th>
    </tr>
    <tr>
      <th>year</th>
      <th>week_number</th>
      <th>row</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1995</td>
      <td>11</td>
      <td>447</td>
      <td>33.0</td>
      <td>28.0</td>
      <td>Nov 2, 1995</td>
      <td>NaN</td>
      <td>Thu</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>24.0</td>
      <td>Virginia</td>
      <td>2.0</td>
      <td>Florida State</td>
      <td>-22.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>5</td>
      <td>309</td>
      <td>38.0</td>
      <td>10.0</td>
      <td>Oct 3, 2015</td>
      <td>7:00 PM</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>25.0</td>
      <td>Florida</td>
      <td>3.0</td>
      <td>Mississippi</td>
      <td>-22.0</td>
      <td>28.0</td>
    </tr>
    <tr>
      <td>2017</td>
      <td>10</td>
      <td>539</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>Oct 28, 2017</td>
      <td>3:30 PM</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>Jack Trice Stadium - Ames, Iowa</td>
      <td>True</td>
      <td>25.0</td>
      <td>Iowa State</td>
      <td>4.0</td>
      <td>Texas Christian</td>
      <td>-21.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <td rowspan="2" valign="top">2014</td>
      <td>9</td>
      <td>514</td>
      <td>10.0</td>
      <td>7.0</td>
      <td>Oct 25, 2014</td>
      <td>7:15 PM</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>24.0</td>
      <td>Louisiana State</td>
      <td>3.0</td>
      <td>Mississippi</td>
      <td>-21.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>378</td>
      <td>37.0</td>
      <td>33.0</td>
      <td>Oct 4, 2014</td>
      <td>3:30 PM</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>25.0</td>
      <td>Texas Christian</td>
      <td>4.0</td>
      <td>Oklahoma</td>
      <td>-21.0</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



We can look at when a winner is not ranked and the loser is ranked 1, which has happened 35 times in the data.


```python
records[(records['winner_rank'].isna()) & (records['loser_rank'] == 1)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>winner_pts</th>
      <th>loser_pts</th>
      <th>game_date</th>
      <th>game_time</th>
      <th>game_day</th>
      <th>game_loc</th>
      <th>notes</th>
      <th>winner_home</th>
      <th>winner_rank</th>
      <th>winner_name</th>
      <th>loser_rank</th>
      <th>loser_name</th>
      <th>rank_diff</th>
      <th>pts_diff</th>
    </tr>
    <tr>
      <th>year</th>
      <th>week_number</th>
      <th>row</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1950</td>
      <td>4</td>
      <td>167</td>
      <td>28.0</td>
      <td>14.0</td>
      <td>Oct 7, 1950</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Purdue</td>
      <td>1.0</td>
      <td>Notre Dame</td>
      <td>NaN</td>
      <td>14.0</td>
    </tr>
    <tr>
      <td>1952</td>
      <td>5</td>
      <td>203</td>
      <td>23.0</td>
      <td>14.0</td>
      <td>Oct 11, 1952</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Ohio State</td>
      <td>1.0</td>
      <td>Wisconsin</td>
      <td>NaN</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>1956</td>
      <td>7</td>
      <td>308</td>
      <td>20.0</td>
      <td>13.0</td>
      <td>Oct 27, 1956</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Illinois</td>
      <td>1.0</td>
      <td>Michigan State</td>
      <td>NaN</td>
      <td>7.0</td>
    </tr>
    <tr>
      <td>1957</td>
      <td>6</td>
      <td>263</td>
      <td>20.0</td>
      <td>13.0</td>
      <td>Oct 19, 1957</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Purdue</td>
      <td>1.0</td>
      <td>Michigan State</td>
      <td>NaN</td>
      <td>7.0</td>
    </tr>
    <tr>
      <td rowspan="2" valign="top">1960</td>
      <td>10</td>
      <td>497</td>
      <td>23.0</td>
      <td>14.0</td>
      <td>Nov 12, 1960</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Purdue</td>
      <td>1.0</td>
      <td>Minnesota</td>
      <td>NaN</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>11</td>
      <td>534</td>
      <td>23.0</td>
      <td>7.0</td>
      <td>Nov 19, 1960</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Kansas</td>
      <td>1.0</td>
      <td>Missouri</td>
      <td>NaN</td>
      <td>16.0</td>
    </tr>
    <tr>
      <td rowspan="2" valign="top">1961</td>
      <td>8</td>
      <td>381</td>
      <td>13.0</td>
      <td>0.0</td>
      <td>Nov 4, 1961</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Minnesota</td>
      <td>1.0</td>
      <td>Michigan State</td>
      <td>NaN</td>
      <td>13.0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>518</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>Nov 18, 1961</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Texas Christian</td>
      <td>1.0</td>
      <td>Texas</td>
      <td>NaN</td>
      <td>6.0</td>
    </tr>
    <tr>
      <td rowspan="2" valign="top">1962</td>
      <td>4</td>
      <td>182</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>Oct 6, 1962</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>UCLA</td>
      <td>1.0</td>
      <td>Ohio State</td>
      <td>NaN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>521</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>Nov 17, 1962</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Georgia Tech</td>
      <td>1.0</td>
      <td>Alabama</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td rowspan="2" valign="top">1964</td>
      <td>3</td>
      <td>81</td>
      <td>27.0</td>
      <td>21.0</td>
      <td>Sep 26, 1964</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Kentucky</td>
      <td>1.0</td>
      <td>Mississippi</td>
      <td>NaN</td>
      <td>6.0</td>
    </tr>
    <tr>
      <td>12</td>
      <td>619</td>
      <td>20.0</td>
      <td>17.0</td>
      <td>Nov 28, 1964</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southern California</td>
      <td>1.0</td>
      <td>Notre Dame</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>1967</td>
      <td>10</td>
      <td>489</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>Nov 11, 1967</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Oregon State</td>
      <td>1.0</td>
      <td>Southern California</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>1972</td>
      <td>1</td>
      <td>28</td>
      <td>20.0</td>
      <td>17.0</td>
      <td>Sep 9, 1972</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>UCLA</td>
      <td>1.0</td>
      <td>Nebraska</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>1974</td>
      <td>10</td>
      <td>575</td>
      <td>16.0</td>
      <td>13.0</td>
      <td>Nov 9, 1974</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Michigan State</td>
      <td>1.0</td>
      <td>Ohio State</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>1976</td>
      <td>10</td>
      <td>609</td>
      <td>16.0</td>
      <td>14.0</td>
      <td>Nov 6, 1976</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Purdue</td>
      <td>1.0</td>
      <td>Michigan</td>
      <td>NaN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td>1977</td>
      <td>8</td>
      <td>504</td>
      <td>16.0</td>
      <td>0.0</td>
      <td>Oct 22, 1977</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Minnesota</td>
      <td>1.0</td>
      <td>Michigan</td>
      <td>NaN</td>
      <td>16.0</td>
    </tr>
    <tr>
      <td>1979</td>
      <td>7</td>
      <td>406</td>
      <td>21.0</td>
      <td>21.0</td>
      <td>Oct 13, 1979</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Stanford</td>
      <td>1.0</td>
      <td>Southern California</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>1980</td>
      <td>10</td>
      <td>558</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>Nov 1, 1980</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Mississippi State</td>
      <td>1.0</td>
      <td>Alabama</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td rowspan="4" valign="top">1981</td>
      <td>2</td>
      <td>99</td>
      <td>21.0</td>
      <td>14.0</td>
      <td>Sep 12, 1981</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Wisconsin</td>
      <td>1.0</td>
      <td>Michigan</td>
      <td>NaN</td>
      <td>7.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>304</td>
      <td>13.0</td>
      <td>10.0</td>
      <td>Oct 10, 1981</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Arizona</td>
      <td>1.0</td>
      <td>Southern California</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>373</td>
      <td>42.0</td>
      <td>11.0</td>
      <td>Oct 17, 1981</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Arkansas</td>
      <td>1.0</td>
      <td>Texas</td>
      <td>NaN</td>
      <td>31.0</td>
    </tr>
    <tr>
      <td>9</td>
      <td>538</td>
      <td>17.0</td>
      <td>14.0</td>
      <td>Oct 31, 1981</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Miami (FL)</td>
      <td>1.0</td>
      <td>Penn State</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>1982</td>
      <td>10</td>
      <td>522</td>
      <td>31.0</td>
      <td>16.0</td>
      <td>Nov 6, 1982</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Notre Dame</td>
      <td>1.0</td>
      <td>Pittsburgh</td>
      <td>NaN</td>
      <td>15.0</td>
    </tr>
    <tr>
      <td>1984</td>
      <td>6</td>
      <td>236</td>
      <td>17.0</td>
      <td>9.0</td>
      <td>Sep 29, 1984</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Syracuse</td>
      <td>1.0</td>
      <td>Nebraska</td>
      <td>NaN</td>
      <td>8.0</td>
    </tr>
    <tr>
      <td>1985</td>
      <td>5</td>
      <td>215</td>
      <td>38.0</td>
      <td>20.0</td>
      <td>Sep 28, 1985</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Tennessee</td>
      <td>1.0</td>
      <td>Auburn</td>
      <td>NaN</td>
      <td>18.0</td>
    </tr>
    <tr>
      <td>1988</td>
      <td>10</td>
      <td>446</td>
      <td>34.0</td>
      <td>30.0</td>
      <td>Oct 29, 1988</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Washington State</td>
      <td>1.0</td>
      <td>UCLA</td>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
    <tr>
      <td rowspan="2" valign="top">1990</td>
      <td>7</td>
      <td>284</td>
      <td>36.0</td>
      <td>31.0</td>
      <td>Oct 6, 1990</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Stanford</td>
      <td>1.0</td>
      <td>Notre Dame</td>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>314</td>
      <td>28.0</td>
      <td>27.0</td>
      <td>Oct 13, 1990</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Michigan State</td>
      <td>1.0</td>
      <td>Michigan</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>1998</td>
      <td>11</td>
      <td>500</td>
      <td>28.0</td>
      <td>24.0</td>
      <td>Nov 7, 1998</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Michigan State</td>
      <td>1.0</td>
      <td>Ohio State</td>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
    <tr>
      <td>2001</td>
      <td>7</td>
      <td>294</td>
      <td>23.0</td>
      <td>20.0</td>
      <td>Oct 13, 2001</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Auburn</td>
      <td>1.0</td>
      <td>Florida</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>12</td>
      <td>597</td>
      <td>30.0</td>
      <td>26.0</td>
      <td>Nov 9, 2002</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Texas A&amp;M</td>
      <td>1.0</td>
      <td>Oklahoma</td>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
    <tr>
      <td rowspan="2" valign="top">2007</td>
      <td>11</td>
      <td>610</td>
      <td>28.0</td>
      <td>21.0</td>
      <td>Nov 10, 2007</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Illinois</td>
      <td>1.0</td>
      <td>Ohio State</td>
      <td>NaN</td>
      <td>7.0</td>
    </tr>
    <tr>
      <td>13</td>
      <td>703</td>
      <td>50.0</td>
      <td>48.0</td>
      <td>Nov 23, 2007</td>
      <td>NaN</td>
      <td>Fri</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Arkansas</td>
      <td>1.0</td>
      <td>Louisiana State</td>
      <td>NaN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>5</td>
      <td>255</td>
      <td>27.0</td>
      <td>21.0</td>
      <td>Sep 25, 2008</td>
      <td>NaN</td>
      <td>Thu</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Oregon State</td>
      <td>1.0</td>
      <td>Southern California</td>
      <td>NaN</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>



We can also look at ties, when the points difference is 0.  The dataset does not break out ties, but still lists one team as a winner.  There are only 786 ties in the dataset up to 1995, when new rules instituted tie breakers.  However, we need to remember that ties are not properly recorded in this dataset.


```python
# ties
print(len(records[records['pts_diff']==0]))
(records[records['pts_diff']==0]).tail(5)
```

    786





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>winner_pts</th>
      <th>loser_pts</th>
      <th>game_date</th>
      <th>game_time</th>
      <th>game_day</th>
      <th>game_loc</th>
      <th>notes</th>
      <th>winner_home</th>
      <th>winner_rank</th>
      <th>winner_name</th>
      <th>loser_rank</th>
      <th>loser_name</th>
      <th>rank_diff</th>
      <th>pts_diff</th>
    </tr>
    <tr>
      <th>year</th>
      <th>week_number</th>
      <th>row</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5" valign="top">1995</td>
      <td>6</td>
      <td>237</td>
      <td>21.0</td>
      <td>21.0</td>
      <td>Sep 30, 1995</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Rice</td>
      <td>NaN</td>
      <td>Army</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td rowspan="2" valign="top">8</td>
      <td>335</td>
      <td>24.0</td>
      <td>24.0</td>
      <td>Oct 14, 1995</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>18.0</td>
      <td>Texas</td>
      <td>13.0</td>
      <td>Oklahoma</td>
      <td>-5.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>339</td>
      <td>28.0</td>
      <td>28.0</td>
      <td>Oct 14, 1995</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Toledo</td>
      <td>NaN</td>
      <td>Miami (OH)</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>436</td>
      <td>21.0</td>
      <td>21.0</td>
      <td>Oct 28, 1995</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>13.0</td>
      <td>Southern California</td>
      <td>17.0</td>
      <td>Washington</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>14</td>
      <td>608</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>Nov 25, 1995</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Illinois</td>
      <td>NaN</td>
      <td>Wisconsin</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



## Lets analyze interactions amongst ranked teams, and between ranked and unranked teams.

First, lets find out how many games there should be with at least one ranked team.  There are 48,899 games, so the total numers of games with at least one ranked and no one ranked should be 48,899.


```python
print('Number of total games:', len(records))

at_least_one_ranked = records[(records['winner_rank'] > 0) | (records['loser_rank'] > 0)]
print('Numbers of games where at least one team is ranked:', len(at_least_one_ranked))

no_ranked = records[(records['winner_rank'].isna()) & (records['loser_rank'].isna())]
print('Numbers of games where no team is ranked:', len(no_ranked))

both_ranked = records[(records['winner_rank'] > 0) & (records['loser_rank'] > 0)]
print('Numbers of games where both teams are ranked:', len(both_ranked))
```

    Number of total games: 48899
    Numbers of games where at least one team is ranked: 14852
    Numbers of games where no team is ranked: 34047
    Numbers of games where both teams are ranked: 2790


Looks like there are two cases in our dataset where teams have the exact same rank.  In these cases the teams were tied for these ranks AND played each other.


```python
records[records['rank_diff']==0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>winner_pts</th>
      <th>loser_pts</th>
      <th>game_date</th>
      <th>game_time</th>
      <th>game_day</th>
      <th>game_loc</th>
      <th>notes</th>
      <th>winner_home</th>
      <th>winner_rank</th>
      <th>winner_name</th>
      <th>loser_rank</th>
      <th>loser_name</th>
      <th>rank_diff</th>
      <th>pts_diff</th>
    </tr>
    <tr>
      <th>year</th>
      <th>week_number</th>
      <th>row</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1992</td>
      <td>10</td>
      <td>438</td>
      <td>52.0</td>
      <td>7.0</td>
      <td>Oct 31, 1992</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>8.0</td>
      <td>Nebraska</td>
      <td>8.0</td>
      <td>Colorado</td>
      <td>0.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <td>1995</td>
      <td>19</td>
      <td>639</td>
      <td>20.0</td>
      <td>14.0</td>
      <td>Jan 1, 1996</td>
      <td>NaN</td>
      <td>Mon</td>
      <td>NaN</td>
      <td>Citrus Bowl (Orlando, FL)</td>
      <td>True</td>
      <td>4.0</td>
      <td>Tennessee</td>
      <td>4.0</td>
      <td>Ohio State</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>



Looks good!  Now lets make a new column for each of the different options for games.  We'll treat these fields as booleans, which will allow us to easily compute the mean and size of each of these categories over years.
* 'both_unranked': Both teams are unranked.
* 'ranked_beats_unranked': A ranked team beats an unranked team.
* 'unranked_beats_ranked': An unranked team beats a ranked team.
* 'lower_beats_higher': A lower ranked team beats a higher ranked team.
* 'higher_beats_lower': A higher ranked team beats a lower ranked team.


```python
both_unranked = records[(records['winner_rank'].isna()) & (records['loser_rank'].isna())]
print('Number of times unranked teams play:', len(both_unranked))
records['both_unranked'] = (records['winner_rank'].isna()) & (records['loser_rank'].isna())

ranked_beats_unranked = records[(records['winner_rank'] > 0) & (records['loser_rank'].isna())]
print('Number of times a ranked team beats an unranked team:', len(ranked_beats_unranked))
records['ranked_beats_unranked'] = (records['winner_rank'] > 0) & (records['loser_rank'].isna())

unranked_beats_ranked = records[(records['winner_rank'].isna()) & (records['loser_rank'] > 0)]
print('Number of times an unranked team upsets a ranked team:', len(unranked_beats_ranked))
records['unranked_beats_ranked'] = (records['winner_rank'].isna()) & (records['loser_rank'] > 0)

lower_beats_higher = both_ranked[both_ranked['rank_diff'] < 0]
print('Number of times an a lower ranked team upsets a higher ranked team:', len(lower_beats_higher))
records['lower_beats_higher'] = (records['winner_rank'] > 0) & (records['loser_rank'] > 0) & (records['rank_diff'] < 0)

higher_beats_lower = both_ranked[both_ranked['rank_diff'] > 0]
print('Number of times an a higher ranked team beats a lower ranked team:', len(higher_beats_lower))
records['higher_beats_lower'] = (records['winner_rank'] > 0) & (records['loser_rank'] > 0) & (records['rank_diff'] > 0)
```

    Number of times unranked teams play: 34047
    Number of times a ranked team beats an unranked team: 9850
    Number of times an unranked team upsets a ranked team: 2212
    Number of times an a lower ranked team upsets a higher ranked team: 1070
    Number of times an a higher ranked team beats a lower ranked team: 1718



```python
records.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>winner_pts</th>
      <th>loser_pts</th>
      <th>game_date</th>
      <th>game_time</th>
      <th>game_day</th>
      <th>game_loc</th>
      <th>notes</th>
      <th>winner_home</th>
      <th>winner_rank</th>
      <th>winner_name</th>
      <th>loser_rank</th>
      <th>loser_name</th>
      <th>rank_diff</th>
      <th>pts_diff</th>
      <th>both_unranked</th>
      <th>ranked_beats_unranked</th>
      <th>unranked_beats_ranked</th>
      <th>lower_beats_higher</th>
      <th>higher_beats_lower</th>
    </tr>
    <tr>
      <th>year</th>
      <th>week_number</th>
      <th>row</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5" valign="top">1950</td>
      <td rowspan="5" valign="top">1</td>
      <td>1</td>
      <td>13.0</td>
      <td>12.0</td>
      <td>Sep 15, 1950</td>
      <td>NaN</td>
      <td>Fri</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Presbyterian</td>
      <td>NaN</td>
      <td>Furman</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14.0</td>
      <td>13.0</td>
      <td>Sep 16, 1950</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>@</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>Brigham Young</td>
      <td>NaN</td>
      <td>Idaho State</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>3</td>
      <td>32.0</td>
      <td>0.0</td>
      <td>Sep 16, 1950</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Cincinnati</td>
      <td>NaN</td>
      <td>Texas-El Paso</td>
      <td>NaN</td>
      <td>32.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>4</td>
      <td>56.0</td>
      <td>0.0</td>
      <td>Sep 16, 1950</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Citadel</td>
      <td>NaN</td>
      <td>Parris Island Marines</td>
      <td>NaN</td>
      <td>56.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>5</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>Sep 16, 1950</td>
      <td>NaN</td>
      <td>Sat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>Drake</td>
      <td>NaN</td>
      <td>Denver</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## Types of Team Interactions Over Time

Are there any trends to how often upsets happen?  If pollsters were doing a good job, we would rarely see unranked teams beat ranked teams, only occasionally see a lower team beat a higher ranked team, usually see higher ranked teams beat lower, and almost always see ranked teams beat unranked teams.  Since we dont have any insight into how much better the 26th best team is compared to the 125th team, we will not be concerned about the fifth type of interaction, unranked teams beating unranked teams.


```python
ratios = records[['both_unranked', 'ranked_beats_unranked', 'higher_beats_lower',
                  'lower_beats_higher', 'unranked_beats_ranked', ]]
```


```python
ratios_sum = ratios.groupby('year').sum()
ratios_mean = ratios.groupby('year').mean()
```

These colors are grouped by level of expected outcome.  Blue are neutral games, darker colors are more extreme, greens are expected, and reds are unexpected.  Therefore, an unranked team beating a ranked team is dark red as it is very unexpected.


```python
colors = ['steelblue', 'darkgreen', 'forestgreen', 'salmon', 'firebrick']
```

We can look at the data as both an area chart of counts of the different types, and an area chart of percentage of types of interactions.


```python
ax = ratios_sum.plot.area(figsize=(12,6), color=colors, title='Stacked Area Chart of Types of Games, Total Games, 1950 to 2018')
ax = ratios_mean.plot.area(figsize=(12,6), color=colors, title='Stacked Area Chart of Types of Games, Averages, 1950 to 2018')
```


![png](output_43_0.png)



![png](output_43_1.png)


However, these plots are still lacking in that there is a lot of information that is not easily accessible.  An interactive plot will make it easier to see this data.


```python
x=ratios_sum.index.to_list()
 
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x, y=ratios_sum['both_unranked'],
    name='Both Unranked',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color=colors[0]),
    stackgroup='one' # define stack group
))
fig.add_trace(go.Scatter(
    x=x, y=ratios_sum['ranked_beats_unranked'],
    name='Ranked Beats Unranked',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color=colors[1]),
    stackgroup='one' # define stack group
))
fig.add_trace(go.Scatter(
    x=x, y=ratios_sum['higher_beats_lower'],
    name='Higher Beats Lower Ranked',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color=colors[2]),
    stackgroup='one' # define stack group
))
fig.add_trace(go.Scatter(
    x=x, y=ratios_sum['lower_beats_higher'],
    name='Lower Beats Higher Ranked',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color=colors[3]),
    stackgroup='one' # define stack group
))
fig.add_trace(go.Scatter(
    x=x, y=ratios_sum['unranked_beats_ranked'],
    name='Unranked Beats Ranked',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color=colors[4]),
    stackgroup='one' # define stack group
))
 
fig.update_layout(title="Stacked Area Chart of Types of Games, Total Games, 1950 to 2018")
fig.show()
```


        <script type="text/javascript">
        window.PlotlyConfig = {MathJaxConfig: 'local'};
        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}
        if (typeof require !== 'undefined') {
        require.undef("plotly");
        define('plotly', function(require, exports, module) {
            /**
* plotly.js v1.49.4
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
* Licensed under the MIT license
*/
        });
        require(['plotly'], function(Plotly) {
            window._Plotly = Plotly;
        });
        }
        </script>




<div>


            <div id="8386f54b-e546-4295-89cd-5cf30921e768" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("8386f54b-e546-4295-89cd-5cf30921e768")) {
                    Plotly.newPlot(
                        '8386f54b-e546-4295-89cd-5cf30921e768',
                        [{"hoverinfo": "x+y", "line": {"color": "steelblue", "width": 0.5}, "mode": "lines", "name": "Both Unranked", "stackgroup": "one", "type": "scatter", "x": [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], "y": [474.0, 455.0, 429.0, 399.0, 416.0, 406.0, 417.0, 420.0, 419.0, 424.0, 434.0, 492.0, 535.0, 524.0, 538.0, 546.0, 542.0, 539.0, 465.0, 478.0, 510.0, 541.0, 547.0, 558.0, 558.0, 605.0, 607.0, 664.0, 614.0, 618.0, 616.0, 599.0, 486.0, 489.0, 468.0, 466.0, 430.0, 432.0, 428.0, 382.0, 390.0, 393.0, 387.0, 384.0, 384.0, 391.0, 403.0, 409.0, 417.0, 431.0, 447.0, 460.0, 492.0, 491.0, 460.0, 466.0, 508.0, 515.0, 534.0, 531.0, 537.0, 544.0, 556.0, 564.0, 594.0, 590.0, 596.0, 600.0, 603.0]}, {"hoverinfo": "x+y", "line": {"color": "darkgreen", "width": 0.5}, "mode": "lines", "name": "Ranked Beats Unranked", "stackgroup": "one", "type": "scatter", "x": [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], "y": [118.0, 115.0, 112.0, 119.0, 105.0, 105.0, 113.0, 104.0, 103.0, 110.0, 106.0, 64.0, 69.0, 71.0, 62.0, 67.0, 73.0, 67.0, 113.0, 134.0, 134.0, 156.0, 134.0, 152.0, 134.0, 137.0, 126.0, 141.0, 139.0, 142.0, 140.0, 135.0, 138.0, 146.0, 131.0, 144.0, 132.0, 138.0, 149.0, 166.0, 170.0, 166.0, 160.0, 163.0, 160.0, 160.0, 182.0, 168.0, 171.0, 157.0, 166.0, 151.0, 179.0, 180.0, 190.0, 156.0, 206.0, 173.0, 175.0, 203.0, 191.0, 194.0, 194.0, 196.0, 180.0, 184.0, 170.0, 187.0, 174.0]}, {"hoverinfo": "x+y", "line": {"color": "forestgreen", "width": 0.5}, "mode": "lines", "name": "Higher Beats Lower Ranked", "stackgroup": "one", "type": "scatter", "x": [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], "y": [18.0, 17.0, 21.0, 20.0, 20.0, 16.0, 17.0, 23.0, 24.0, 19.0, 15.0, 10.0, 7.0, 1.0, 7.0, 3.0, 6.0, 3.0, 20.0, 22.0, 18.0, 18.0, 25.0, 24.0, 17.0, 25.0, 22.0, 20.0, 22.0, 16.0, 22.0, 19.0, 24.0, 19.0, 19.0, 16.0, 18.0, 29.0, 24.0, 31.0, 23.0, 39.0, 36.0, 33.0, 29.0, 32.0, 28.0, 37.0, 39.0, 35.0, 33.0, 38.0, 37.0, 32.0, 25.0, 32.0, 31.0, 37.0, 39.0, 31.0, 44.0, 40.0, 38.0, 32.0, 39.0, 34.0, 34.0, 37.0, 37.0]}, {"hoverinfo": "x+y", "line": {"color": "salmon", "width": 0.5}, "mode": "lines", "name": "Lower Beats Higher Ranked", "stackgroup": "one", "type": "scatter", "x": [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], "y": [7.0, 11.0, 14.0, 7.0, 15.0, 13.0, 13.0, 11.0, 8.0, 16.0, 16.0, 2.0, 4.0, 8.0, 4.0, 8.0, 4.0, 4.0, 14.0, 11.0, 11.0, 9.0, 11.0, 8.0, 11.0, 12.0, 19.0, 13.0, 14.0, 18.0, 14.0, 13.0, 12.0, 13.0, 19.0, 22.0, 21.0, 12.0, 15.0, 20.0, 24.0, 18.0, 20.0, 27.0, 24.0, 25.0, 19.0, 15.0, 17.0, 23.0, 19.0, 19.0, 18.0, 23.0, 15.0, 20.0, 17.0, 16.0, 22.0, 19.0, 19.0, 21.0, 16.0, 23.0, 26.0, 24.0, 22.0, 21.0, 21.0]}, {"hoverinfo": "x+y", "line": {"color": "firebrick", "width": 0.5}, "mode": "lines", "name": "Unranked Beats Ranked", "stackgroup": "one", "type": "scatter", "x": [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], "y": [34.0, 27.0, 24.0, 30.0, 30.0, 35.0, 27.0, 32.0, 36.0, 28.0, 32.0, 23.0, 16.0, 17.0, 23.0, 20.0, 13.0, 23.0, 32.0, 16.0, 32.0, 24.0, 27.0, 20.0, 45.0, 27.0, 30.0, 29.0, 27.0, 31.0, 24.0, 38.0, 27.0, 29.0, 39.0, 25.0, 36.0, 22.0, 20.0, 33.0, 39.0, 23.0, 33.0, 25.0, 39.0, 31.0, 30.0, 37.0, 30.0, 40.0, 37.0, 41.0, 46.0, 45.0, 34.0, 44.0, 30.0, 57.0, 54.0, 51.0, 35.0, 35.0, 36.0, 34.0, 31.0, 39.0, 51.0, 33.0, 49.0]}],
                        {"template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Stacked Area Chart of Types of Games, Total Games, 1950 to 2018"}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('8386f54b-e546-4295-89cd-5cf30921e768');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x, y=ratios_sum['both_unranked'],
    name='Both Unranked',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color=colors[0]),
    stackgroup='one', # define stack group
    groupnorm='percent'
))
fig.add_trace(go.Scatter(
    x=x, y=ratios_sum['ranked_beats_unranked'],
    name='Ranked Beats Unranked',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color=colors[1]),
    stackgroup='one', # define stack group
    groupnorm='percent'
))
fig.add_trace(go.Scatter(
    x=x, y=ratios_sum['higher_beats_lower'],
    name='Higher Beats Lower Ranked',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color=colors[2]),
    stackgroup='one', # define stack group
))
fig.add_trace(go.Scatter(
    x=x, y=ratios_sum['lower_beats_higher'],
    name='Lower Beats Higher Ranked',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color=colors[3]),
    stackgroup='one', # define stack group
    groupnorm='percent'
))
fig.add_trace(go.Scatter(
    x=x, y=ratios_sum['unranked_beats_ranked'],
    name='Unranked Beats Ranked',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color=colors[4]),
    stackgroup='one', # define stack group
    groupnorm='percent'
))
fig.update_layout(
    showlegend=True,
    yaxis=dict(
        type='linear',
        range=[1, 100],
        ticksuffix='%'))
fig.update_layout(title="Stacked Area Chart of Types of Games, Percentage, 1950 to 2018")
fig.show()
```


<div>


            <div id="4faec447-2c14-4267-8041-b166c890c490" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("4faec447-2c14-4267-8041-b166c890c490")) {
                    Plotly.newPlot(
                        '4faec447-2c14-4267-8041-b166c890c490',
                        [{"groupnorm": "percent", "hoverinfo": "x+y", "line": {"color": "steelblue", "width": 0.5}, "mode": "lines", "name": "Both Unranked", "stackgroup": "one", "type": "scatter", "x": [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], "y": [474.0, 455.0, 429.0, 399.0, 416.0, 406.0, 417.0, 420.0, 419.0, 424.0, 434.0, 492.0, 535.0, 524.0, 538.0, 546.0, 542.0, 539.0, 465.0, 478.0, 510.0, 541.0, 547.0, 558.0, 558.0, 605.0, 607.0, 664.0, 614.0, 618.0, 616.0, 599.0, 486.0, 489.0, 468.0, 466.0, 430.0, 432.0, 428.0, 382.0, 390.0, 393.0, 387.0, 384.0, 384.0, 391.0, 403.0, 409.0, 417.0, 431.0, 447.0, 460.0, 492.0, 491.0, 460.0, 466.0, 508.0, 515.0, 534.0, 531.0, 537.0, 544.0, 556.0, 564.0, 594.0, 590.0, 596.0, 600.0, 603.0]}, {"groupnorm": "percent", "hoverinfo": "x+y", "line": {"color": "darkgreen", "width": 0.5}, "mode": "lines", "name": "Ranked Beats Unranked", "stackgroup": "one", "type": "scatter", "x": [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], "y": [118.0, 115.0, 112.0, 119.0, 105.0, 105.0, 113.0, 104.0, 103.0, 110.0, 106.0, 64.0, 69.0, 71.0, 62.0, 67.0, 73.0, 67.0, 113.0, 134.0, 134.0, 156.0, 134.0, 152.0, 134.0, 137.0, 126.0, 141.0, 139.0, 142.0, 140.0, 135.0, 138.0, 146.0, 131.0, 144.0, 132.0, 138.0, 149.0, 166.0, 170.0, 166.0, 160.0, 163.0, 160.0, 160.0, 182.0, 168.0, 171.0, 157.0, 166.0, 151.0, 179.0, 180.0, 190.0, 156.0, 206.0, 173.0, 175.0, 203.0, 191.0, 194.0, 194.0, 196.0, 180.0, 184.0, 170.0, 187.0, 174.0]}, {"hoverinfo": "x+y", "line": {"color": "forestgreen", "width": 0.5}, "mode": "lines", "name": "Higher Beats Lower Ranked", "stackgroup": "one", "type": "scatter", "x": [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], "y": [18.0, 17.0, 21.0, 20.0, 20.0, 16.0, 17.0, 23.0, 24.0, 19.0, 15.0, 10.0, 7.0, 1.0, 7.0, 3.0, 6.0, 3.0, 20.0, 22.0, 18.0, 18.0, 25.0, 24.0, 17.0, 25.0, 22.0, 20.0, 22.0, 16.0, 22.0, 19.0, 24.0, 19.0, 19.0, 16.0, 18.0, 29.0, 24.0, 31.0, 23.0, 39.0, 36.0, 33.0, 29.0, 32.0, 28.0, 37.0, 39.0, 35.0, 33.0, 38.0, 37.0, 32.0, 25.0, 32.0, 31.0, 37.0, 39.0, 31.0, 44.0, 40.0, 38.0, 32.0, 39.0, 34.0, 34.0, 37.0, 37.0]}, {"groupnorm": "percent", "hoverinfo": "x+y", "line": {"color": "salmon", "width": 0.5}, "mode": "lines", "name": "Lower Beats Higher Ranked", "stackgroup": "one", "type": "scatter", "x": [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], "y": [7.0, 11.0, 14.0, 7.0, 15.0, 13.0, 13.0, 11.0, 8.0, 16.0, 16.0, 2.0, 4.0, 8.0, 4.0, 8.0, 4.0, 4.0, 14.0, 11.0, 11.0, 9.0, 11.0, 8.0, 11.0, 12.0, 19.0, 13.0, 14.0, 18.0, 14.0, 13.0, 12.0, 13.0, 19.0, 22.0, 21.0, 12.0, 15.0, 20.0, 24.0, 18.0, 20.0, 27.0, 24.0, 25.0, 19.0, 15.0, 17.0, 23.0, 19.0, 19.0, 18.0, 23.0, 15.0, 20.0, 17.0, 16.0, 22.0, 19.0, 19.0, 21.0, 16.0, 23.0, 26.0, 24.0, 22.0, 21.0, 21.0]}, {"groupnorm": "percent", "hoverinfo": "x+y", "line": {"color": "firebrick", "width": 0.5}, "mode": "lines", "name": "Unranked Beats Ranked", "stackgroup": "one", "type": "scatter", "x": [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], "y": [34.0, 27.0, 24.0, 30.0, 30.0, 35.0, 27.0, 32.0, 36.0, 28.0, 32.0, 23.0, 16.0, 17.0, 23.0, 20.0, 13.0, 23.0, 32.0, 16.0, 32.0, 24.0, 27.0, 20.0, 45.0, 27.0, 30.0, 29.0, 27.0, 31.0, 24.0, 38.0, 27.0, 29.0, 39.0, 25.0, 36.0, 22.0, 20.0, 33.0, 39.0, 23.0, 33.0, 25.0, 39.0, 31.0, 30.0, 37.0, 30.0, 40.0, 37.0, 41.0, 46.0, 45.0, 34.0, 44.0, 30.0, 57.0, 54.0, 51.0, 35.0, 35.0, 36.0, 34.0, 31.0, 39.0, 51.0, 33.0, 49.0]}],
                        {"showlegend": true, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Stacked Area Chart of Types of Games, Percentage, 1950 to 2018"}, "yaxis": {"range": [1, 100], "ticksuffix": "%", "type": "linear"}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('4faec447-2c14-4267-8041-b166c890c490');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


We can look for the most 'accurate' years by computing the correct answers (ranked beats unranked, and higher beats lower) and the incorrect answers (unranked beats ranked, and lower beats higher).  Then we can find the difference between the correct answers and incorrect answers to get a rough metric for accuracy.


```python
ratios_years = ratios.groupby('year').mean()
```


```python
ratios_years['correct'] = ratios_years['ranked_beats_unranked'] + ratios_years['higher_beats_lower']
ratios_years['incorrect'] = ratios_years['lower_beats_higher'] + ratios_years['unranked_beats_ranked']
ratios_years['accuracy'] = ratios_years['correct'] - ratios_years['incorrect']
```


```python
acc_df = ratios_years[['correct','incorrect','accuracy']]

acc_df.plot(figsize=(12,6), color=('g','r','black'), style=['--','--','-'], linewidth=3, 
            title="Correct, Incorrect, and Overall Accuracy of AP Poll in Games between Ranked Teams, 1950 to 2018")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x139240d10>




![png](output_50_1.png)


Looks like by far the worst years for accuracy were in the 60s.  College football at the time was still dealing with intense issues of segregation with many teams in the south still not allowing African-Americans to play.  Additionally, some of these teams did not want to play racially integrated teams.  This could be a reason for the inaccuracies of the polls.  


```python
labels = ['Both Unranked', 'Ranked Beats Unranked', 'Higher Beats Lower Ranked',
       'Lower Bears Higher Ranked', 'Unranked Beats Ranked']

fig = go.Figure(data=[go.Pie(labels=labels, values=ratios.sum().to_list(), hole=.2, 
                             direction = 'clockwise', sort=False, )])
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=16,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.update_layout(title="Pie Chart of Types of Team Interactions, 1950 to 2018")
fig.show()
```


<div>


            <div id="d830b6e1-2c56-414d-90a2-f6bc59c84347" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("d830b6e1-2c56-414d-90a2-f6bc59c84347")) {
                    Plotly.newPlot(
                        'd830b6e1-2c56-414d-90a2-f6bc59c84347',
                        [{"direction": "clockwise", "hole": 0.2, "hoverinfo": "label+value", "labels": ["Both Unranked", "Ranked Beats Unranked", "Higher Beats Lower Ranked", "Lower Bears Higher Ranked", "Unranked Beats Ranked"], "marker": {"colors": ["steelblue", "darkgreen", "forestgreen", "salmon", "firebrick"], "line": {"color": "#000000", "width": 2}}, "sort": false, "textfont": {"size": 16}, "textinfo": "percent", "type": "pie", "values": [34047, 9850, 1718, 1070, 2212]}],
                        {"template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Pie Chart of Types of Team Interactions, 1950 to 2018"}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('d830b6e1-2c56-414d-90a2-f6bc59c84347');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
year = 2018
labels = ['Both Unranked', 'Ranked Beats Unranked', 'Higher Beats Lower Ranked',
       'Lower Bears Higher Ranked', 'Unranked Beats Ranked']

fig = go.Figure(data=[go.Pie(labels=labels, values=ratios.groupby('year').mean().loc[year].to_list(), hole=.2, 
                             direction = 'clockwise', sort=False, )])
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=16,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.update_layout(title="Pie Chart of Types of Team Interaction, {}".format(year))
fig.show()
```


<div>


            <div id="085c2688-908c-4cf3-a546-4f917c4bb1d1" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("085c2688-908c-4cf3-a546-4f917c4bb1d1")) {
                    Plotly.newPlot(
                        '085c2688-908c-4cf3-a546-4f917c4bb1d1',
                        [{"direction": "clockwise", "hole": 0.2, "hoverinfo": "label+value", "labels": ["Both Unranked", "Ranked Beats Unranked", "Higher Beats Lower Ranked", "Lower Bears Higher Ranked", "Unranked Beats Ranked"], "marker": {"colors": ["steelblue", "darkgreen", "forestgreen", "salmon", "firebrick"], "line": {"color": "#000000", "width": 2}}, "sort": false, "textfont": {"size": 16}, "textinfo": "percent", "type": "pie", "values": [0.6821266968325792, 0.19683257918552036, 0.0418552036199095, 0.023755656108597284, 0.05542986425339366]}],
                        {"template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Pie Chart of Types of Team Interaction, 2018"}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('085c2688-908c-4cf3-a546-4f917c4bb1d1');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>
