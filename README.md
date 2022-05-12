# The case of the avocado
__Authors: Zachary Zhang, Eric Kim, Daniel Lee__

# Research Questions
1.  `AveragePrice` vs `TotalVolume`. How do they compare, is there a correlation between the two, and what are the general trends? We would have 3 plots, 1 is to plot the overall U.S. to see general trends. The other two plots would be seeing the trends in each state. 

2. 

3. 


# Motivation
As we all know avocados are the bane of millennials, avocado toast is too tantalizing for millennials to resist which is why they have such poor fiscal responsibility and is the reason why the middle class is shrinking. Or is it?

The purpose of our analysis here is to first determine the general trends of avocados. 

# Dataset
https://www.kaggle.com/datasets/valentinjoseph/avocado-sales-20152021-us-centric is an [updated dataset](https://www.kaggle.com/datasets/neuromusic/avocado-prices) that contains observed avocado sales data that the [Hass Avocada Board](https://hassavocadoboard.com/) collected from 2015 to 2021. It was created by Valentin Joseph to add additional observations up to 2021. The [original dataset](https://www.kaggle.com/datasets/neuromusic/avocado-prices) created by Justin Kiggins only went from 2015-2018. 

The dataset contains 13 columns. Each row is a recorded observation. 
| Column| Description |
| ---   | ---         |
| Date | The date the observation was recorded |
| AveragePrice | The average price of the sold avocados in the observation |
| TotalVolume | Total volume of sold avocados in the observation |
| plu4046 | The amount [Small/Medium Hass Avocado (~3-5oz avocado)](https://loveonetoday.com/how-to/identify-hass-avocados/) sold in the observation |
| plu4225 | The amount [Large Hass Avocado (~8-10oz avocado)](https://loveonetoday.com/how-to/identify-hass-avocados/) sold in the observation |
| plu4770 | The amount of [Extra Large Hass Avocado (~10-15oz avocado)](https://loveonetoday.com/how-to/identify-hass-avocados/) sold in the observation |
| TotalBags | Total number of avocados bags sold in the observation |
| SmallBags |  Total number of small avocado bags sold in the observation |
| LargeBags | Total number of large avocado bags sold in the observation  |
| XLargeBags | Total number of extra-large avocado bags sold in the observation  |
| type | Type of avacado can either be `organic` or `conventional` |
| year | The year the observation was recorded |
| region | The geographic location where the observation was recorded. Geographic locations can be states, cities, US regions, and more |

# Challenge Goals
1. A challenge goal we want to do is use `plotly` for our plotting needs. It would be primarily for question #1. It would be interesting to see the trend of each state for avocado data on a map instead of using a line plot. If it is to difficult we can just use a stacked line chart from `Seaborn`.

2. 

# Method
1. For question #1, first be able to plot anything with `plotly`, we will need geospatial data. Unfortunately, our avocado dataset does not come with geospatial data so we will need to load external geospatial data for the U.S. We might have to do a join. From there we will be able to create Choropleth plots. For `AveragePrice` vs `TotalVolume` the two columns would be plotted onto one graph using `subplots()` from `matplotlib.pyplot` as a stacked line plot. After loading in the geospatial data we can plot two seperate Choropleth plots. Ideally we would want to have a time component but initially it will be either one chosen year or an aggregate of all the observations. 

2. 

3. 

# Work Plan