# The case of the avocado
__Authors: Zachary Zhang, Eric Kim, Daniel Lee__

# Research Questions
1.  `AveragePrice` vs `TotalVolume`. How do they compare, is there a correlation between the two, and what are the general trends? We would have 3 plots, 1 is to plot the overall U.S. to see general trends. The other two plots would be seeing the trends in each state. 

2. Do the prices of avocados reflect their yield? In other words, how would an avocado's price be affected by how many avocados were produced for a time period (in our case, a year)? Adding on to this, if there was some sort of correlation between the yield of avocados and their prices, could this be reflected for other fruits as well? For this question, we'd have two graphs: one graph would compare the yield of avocados versus their prices, and the second graph would compare this trend with another fruit's yield trend (in our case, apples).

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

http://data.un.org/Data.aspx?d=FAO&f=itemCode:572&c=2,4,5,6,7&s=countryName:asc,elementCode:asc,year:desc&v=4 is a dataset that shows the area harvested, the total yield and production emissions for avocados in every country, as well as total count for the entire world. It is provided by the Food and Agriculture Organization and provides data from 1961 to 2018. 

The dataset contains 5 columns. Each row contains a specific statistic for the production and yield of all avocados.
| Column| Description |
| ---   | ---         |
| Country or Area | The place the observations were made |
| Element | The type of statistic recorded (This can be `Area Harvested`, `Yield` or `Production`) |
| Year | The year the statistic was recorded |
| Unit | The unit of the element recorded |
| Value | The total amount of element that was recorded |

http://data.un.org/Data.aspx?d=FAO&f=itemCode:515&c=2,4,5,6,7&s=countryName:asc,elementCode:asc,year:desc&v=14 is a dataset that shows the area harvested, the total yield and production emissions for apples in every country, as well as total count for the entire world. It is provided by the Food and Agriculture Organization and provides data from 1961 to 2018.

The dataset contains 5 columns. Each row contains a specific statistic for the production and yield of all apples.
| Column| Description |
| ---   | ---         |
| Country or Area | The place the observations were made |
| Element | The type of statistic recorded (This can be `Area Harvested`, `Yield` or `Production`) |
| Year | The year the statistic was recorded |
| Unit | The unit of the element recorded |
| Value | The total amount of element that was recorded |

# Challenge Goals
1. A challenge goal we want to do is use `plotly` for our plotting needs. It would be primarily for question #1. It would be interesting to see the trend of each state for avocado data on a map instead of using a line plot. If it is to difficult we can just use a stacked line chart from `Seaborn`.

2. Our second challenge goal we want to do is to try and combine **multiple datasets** together to try and form trends that answer our research questions. For example, for question 2 we want to use multiple datasets in order to try and recognize trends between avocado prices and yields, and we also want to compare our trends for avocado yields to other fruits to try and see if yield trends are universal or dependent on the fruit.

# Method
1. For question #1, first be able to plot anything with `plotly`, we will need geospatial data. Unfortunately, our avocado dataset does not come with geospatial data so we will need to load external geospatial data for the U.S. We might have to do a join. From there we will be able to create Choropleth plots. For `AveragePrice` vs `TotalVolume` the two columns would be plotted onto one graph using `subplots()` from `matplotlib.pyplot` as a stacked line plot. After loading in the geospatial data we can plot two seperate Choropleth plots. Ideally we would want to have a time component but initially it will be either one chosen year or an aggregate of all the observations. 

2. For question #2, filtering all the data is incredibly important to create the right kind of trends that we want to make. For the avocado prices, we'd want to pick a location (in our case, it would be the Americas) and time range to take our data from, and then pick out the data that only pertains to our research question. For our second question, we'd only want the prices of avocados sold as well as the total volume and bags of avocados that were sold. From our bigger yield dataset, we'd only want the Americas as well as the `yield` with our selected time range. We'd then construct two graphs, one that shows the price versus the yield, and then compare this trend with our `apples` dataset with another graph. This may change as we put it into practice, but this would be a general outline for what we'd want to do.

3. 

# Work Plan

For working together on this project we have a [GitHub repository](https://github.com/Frey-mond/avocados). We are all going to be using VSCode and there is an
automatic flake8 lintr that runs on every commit. If any of us runs into unexpected challenges, we have a group chat for communicating.