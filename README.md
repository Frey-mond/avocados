# The case of the avocado
__Authors: Zachary Zhang, Eric Kim, Daniel Lee__

# Research Questions
1.  `AveragePrice` vs `TotalVolume`. How do they compare, is there a correlation between the two, and what are the general trends? We would have 4 plots, two are to plot the overall U.S. to see general trends. The other two plots would be seeing the trends in each state. 

2. 

3. 


# Motivation
As we all know avocados are the bane of millennials, avocado toast is too tantalizing for millennials to resist which is why they have such poor fiscal responsibility and is the reason why the middle class is shrinking. Or is it?

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

# Challenge goals
1. A challenge goal we want to do is use `plotly` for our plotting needs. It would be primarily for question #1. It would be interesting to see the trend of each state for avocado data on a map instead of using a line plot. If it is to difficult we can just use a stacked line chart from `Seaborn`.

2. 

# Method

# Work Plan