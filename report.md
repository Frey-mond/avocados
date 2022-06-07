# The Case of the Avocado

Authors: Zachary Zhang, Eric Kim, Daniel Lee

## Tables of Contents

1. [Research Questions](#research-questions)
2. [Motivation](#motivation)
3. [Dataset](#dataset)
    1. [Avocado](#avocado)
    2. [Avocado Production](#avocado-production)
    3. [Apples](#apples)
    4. [Income by Age Group](#income-by-age-group)
4. [Challenge Goals](#challenge-goals)
5. [Method](#method)
6. [Work Plan](#work-plan)
    1. [Time Table](#time-table)
7. [Results](#results)
    1. [Task 1](#task-1)
    2. [Task 2](#task-2)
    3. [Task 3](#task-3)
8. [Impact and Limiations](#impact-and-limications)
9. [Work Plan Evaluation](#work-plan-evaluation)
10. [Testing](#testing)
11. [Resources Used](#resources-used)

## Research Questions

1. Question: `AveragePrice` vs `TotalVolume`. How do they compare, is there a correlation between the two, and what are the general trends? We would have 3 plots, 1 is to plot
the trends in Seattle. The other two plots would be to see the overall trend in the US.

    Result: Generally there is a correlation between the average price of avocados and total volume except for organic avocados. Also the most popular bags sold in Seattle are small avocado bags.

2. Question: Do the prices of avocados reflect their yield? In other words, how would an avocado's price be affected by how many avocados were produced for a time period
(in our case, a year)? Adding on to this, if there was some sort of correlation between the yield of avocados and their prices, could this be reflected for other
fruits as well? For this question, we'd have two graphs: one graph would compare the yield of avocados versus their prices, and the second graph would compare this
trend with another fruit's yield trend (in our case, apples).

    Result: There was indeed a correlation between the price of an avocado and the yield of an avocado. From 2015 to 2017 we saw that both the price and yield of avocados were steadily increasing. However, from 2018 onwards we saw that while the price of an avocado was decreasing, the yield of avocados drastically slowed down, to where the trend was the slowest out of the years. We also saw a slight correlation between avocados and apples - from 2015 to 2017, we saw that both fruits had an upward trend and were both being produced at a sharp rate, but when 2018 came, the yield of avocados slowed down significantly, but even more interestingly was that the yield of apples actually started to plummet.

3. Question: Can we use the income of people to predict the price of avocados? Does a higher income mean that people can afford to spend more on avocados? We will implement a model
that predicts the price of avocados based on the mean and median incomes of various age groups.

    Result:

## Motivation

As we all know avocados are the bane of millennials, avocado toast is too tantalizing for millennials to resist which is why they have such poor fiscal responsibility
and is the reason why the middle class is shrinking. Or is it? We propose to examine avocados and their devious nature in the hopes of determing the veracity of the
previous statements.

The purpose of our analysis here is to first determine the general trends of avocados. We are curious about the general feel of how avocados are doing in the U.S.
This is to help us establish an overall feel of our avocado dataset. We also look at how other factors can affect avocados. Lastly we want to take a stab at determining
whether or not avocado toast is really what is causing the downfall of the middle class.

## Dataset

### Avocado

<https://www.kaggle.com/datasets/valentinjoseph/avocado-sales-20152021-us-centric> is an [updated dataset](https://www.kaggle.com/datasets/neuromusic/avocado-prices)
that contains observed avocado sales data that the [Hass Avocada Board](https://hassavocadoboard.com/) collected from 2015 to 2021. It was created by Valentin Joseph
to add additional observations up to 2021. The [original dataset](https://www.kaggle.com/datasets/neuromusic/avocado-prices) created by Justin Kiggins only went from
2015-2018.

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

### Avocado Production

<http://data.un.org/Data.aspx?d=FAO&f=itemCode:572&c=2,4,5,6,7&s=countryName:asc,elementCode:asc,year:desc&v=4> is a dataset that shows the area harvested, the total
yield and production emissions for avocados in every country, as well as total count for the entire world. It is provided by the Food and Agriculture Organization and
provides data from 1961 to 2018.

The dataset contains 5 columns. Each row contains a specific statistic for the production and yield of all avocados.
| Column| Description |
| ---   | ---         |
| Country or Area | The place the observations were made |
| Element | The type of statistic recorded (This can be `Area Harvested`, `Yield` or `Production`) |
| Year | The year the statistic was recorded |
| Unit | The unit of the element recorded |
| Value | The total amount of element that was recorded |

### Apples

<http://data.un.org/Data.aspx?d=FAO&f=itemCode:515&c=2,4,5,6,7&s=countryName:asc,elementCode:asc,year:desc&v=14> is a dataset that shows the area harvested, the
total yield and production emissions for apples in every country, as well as total count for the entire world. It is provided by the Food and Agriculture Organization
and provides data from 1961 to 2018.

The dataset contains 5 columns. Each row contains a specific statistic for the production and yield of all apples.
| Column| Description |
| ---   | ---         |
| Country or Area | The place the observations were made |
| Element | The type of statistic recorded (This can be `Area Harvested`, `Yield` or `Production`) |
| Year | The year the statistic was recorded |
| Unit | The unit of the element recorded |
| Value | The total amount of element that was recorded |

### Income by Age Group

<https://www.census.gov/data/tables/time-series/demo/income-poverty/historical-income-families.html> is a dataset taken from the US Census website that shows the mean and median income of different age groups in units of the given year's dollars and dollars adjusted for inflation in 2020.
The data ranges from 1947 to 2020 and covers income data for all ages and subgroups 15-24, 25-34, 35-44, 45-54, 55-64, and 65+.

The data set contains 6 columns:
| Column| Description |
| ---   | ---         |
| Age and year | The age range of the sampled set (before table) or the year the data was observed (in table) |
| Number (thousands) | The number of households in thousands observed |
| Median Dollars (Current) | The median income in that year's dollars |
| Median Dollars (2020) | The median income adjusted to 2020 inflation |
| Mean Dollars (Current) | The mean income in that year's dollars |
| Mean Dollars (2020) | The mean income adjusted to 2020 inflation |

## Challenge Goals

1. A challenge goal we want to do is use `plotly` for our plotting needs and __New Library__ as a new library to learn. It would be primarily for question #1.
It would be interesting to see the trend of each city for avocado data on a map instead of using a line plot. If it is to difficult we can just use a stacked line
chart from `Seaborn`.

    In the original proposal for question 1, we wanted to graph avocado data with geometries. Unfortunately the `region` column in the dataset was very
    inconsistent in its formatting. Some strings had no space others others had space for each word. The different regions included were very confusing.
    There were some cities, a couple of states and some general regions of the US. Due to these issues we elected to plot avocado data in Seattle
    and accross the entire US.

2. Our second challenge goal we want to do is to try and combine __multiple datasets__ together to try and form trends that answer our research questions. For example,
for question 2 we want to use multiple datasets in order to try and recognize trends between avocado prices and yields, and we also want to compare our trends for avocado
yields to other fruits to try and see if yield trends are universal or dependent on the fruit.

## Method

1. For question #1 we have to clean up the columns in the avocado dataaset due to inconsistencies in how the string data was formmated. We might have to do a join. We
will also have to filter `region` to only cities. From there we will be able to create Choropleth plots. For `AveragePrice` vs `TotalVolume` the two columns would be
plotted onto one graph using `subplots()` from `matplotlib.pyplot` as a stacked line plot. After loading in the geospatial data we can plot two seperate Choropleth plots.
Ideally we would want to have a time component using `year` or `Date` but initially it will be either one chosen year or an aggregate of all the observations. By plotting
`AveragePrice` vs `TotalVolume` on one  graph, we should hopefully be able to see trends and potential correlation between the two columns. For the Chorpleth plot we will
be able to see how cities differ and maybe regional differences or similarities.

2. For question #2, filtering all the data is incredibly important to create the right kind of trends that we want to make. For the avocado prices, we'd want to pick
a location (in our case, it would be the Americas) and time range to take our data from, and then pick out the data that only pertains to our research question.
For our second question, we'd only want the prices of avocados sold as well as the total volume and bags of avocados that were sold. From our bigger yield
dataset, we'd only want the Americas as well as the `yield` with our selected time range. We'd then construct two graphs, one that shows the price versus the yield,
and then compare this trend with our `apples` dataset with another graph. This may change as we put it into practice, but this would be a general outline for what
we'd want to do.

3. For question #3, we plan on using the `Mean Dollars (Current)` and `Median Dollars (Current)` joined with `AveragePrice` to form our dataset for our ML model.
We will filter the data from f11ar.csv to only contain years from 2015-2020 to match the avocado data we have. Then, we will use `scikit-learn` to
make a ML model to predict the price of avocados based on the median and mean incomes of various age groups, specifically using a `DecisionTreeRegressor`.
We will then implement an 80/20 split into training and test data. However, given the relatively small number of parameters to pass in as features, we can expect that the
model will underfit the dataset. Should the training and testing `accuracy-scores` be on the lower side, we can say for certain.

## Work Plan

For working together on this project we have a [GitHub repository](https://github.com/Frey-mond/avocados). We are all going to be using VSCode and there is an
automatic flake8 linter that runs on every commit. If any of us runs into unexpected challenges, we have a group chat for communicating. We are going to be working
on the questions in parallel in our Python files and working on the challenges when it makes sense to.
We will split up the work based on the questions. Each question will be split into it's own file. Any code shared between the questions will be put into its own file and imported.

### Time Table

| Tasks | Time Estimate |
| ---   | ---           |
| Question 1| 6-7 hours |
| Question 2 | 8-9 hours |
| Question 3 | 10-12 hours |
| Style and Testing | 25-30 hours (cumulative) |
| Writeup | 10-15 hours |

## Results

### Task 1

![Total US Avocado Volume Per Business Quarter](https://raw.githubusercontent.com/Frey-mond/avocados/main/output/volume.png)

Looking at the graph of total volume of US avocado sales, we see an increase overtime. There are quarter to quarter fluctuations with
peaks generally the spring and falls in the winter. This makes sense because like all fruits, they having a growing season. When supply
and quality of avocados fall so will demand. There is a massive drop in the winter of 2021 where the total volume of avocados
falls by 50% compared to the summer of 2021. This could be a result of COVID cases surging in the sametime frame.

![Average Avocado Price Per Quarter](https://raw.githubusercontent.com/Frey-mond/avocados/main/output/average_price.png)

For the average price of avocados, the price is fairly consistent with a slight upwards trend. The quarter to quarter
fluctuation could be caused by the cost with growing the avocados.

![Average Price Vs Total Volume](https://raw.githubusercontent.com/Frey-mond/avocados/main/output/volume_vs_price.png)

When comparing the average price of avocados and the total volume, two interesting trends occur. We see on the left graph that
conventional avocados have a negative correlation between the price and volume. The economics of scale means that the more
volume there is, the lower the price would be.

But on the right, when looking at organic avocados there is no correlation. The price of organic avocados is correlated with
something else. A potential cause for this might be because the volume of avocado sales is low and an increase in the cost of
growing organic avocados.

![Volume of Avocado Bags Sold in Seattle](https://raw.githubusercontent.com/Frey-mond/avocados/main/output/seattle.png)

When we look at Seattle the number one thing is that there is a 3 year gap in the data which means we won't have a very good
picture of whats going on. Graphing the volume of different avocado bags shows that small bags are by far the most popular in
Seattle. What's interesting is that there is an increase in sales in the beginning of 2016 to the end of July of 2017. Also
conventional avocados make up the vast majority of sales. With large bags, organic avocados were more popular. And Xlarge bags
saw a giant increase in popularity in 2021.

### Task 2
![Average Price of an Avocado from 2015 to 2018](https://raw.githubusercontent.com/Frey-mond/avocados/main/output/avocado_sales.png)
![Yearly Yield of Avocados from 2015 to 2018](https://raw.githubusercontent.com/Frey-mond/avocados/main/output/avocado_yield.png)

First, looking at these two graphs we can see that from 2015 to 2016, there was an increase in both avocado prices as well as
avocado yields. It's hard to say whether or not the trend for the price line up exactly with how much was produced, but we can
definitely see an increase for both of these factors. From 2016 to 2017, we can see that both the yield and price are increasing
still, but the price increase is much more drastic this time around. This is interesting because the yield from 2016 to 2017 is
only marginally more than the yield from 2015 to 2016, which could indicate other external factors affecting the price jump of
the avocado. However, the most interesting trend here is from 2017 to 2018. We can see that the yield from 2017 to 2018
drastically decreases (around 1500 avocados less compared to 2015 - 2017) to around 
### Task 3

## Impact and Limications

There are some major limitations of our results. For question #1 we saw that there is a correlation on between volume and
average price for avocados but we did not establish that it is a causal relationship. We also didn't account for any
extenuating factors. Our data only uses data gathered by the Hass Avocado Board which only collected data on hass avocados.
This analysis wouldn't apply to other avocado types.

## Work Plan Evaluation

## Testing

## Resources Used

[Plotly Documentation](https://plotly.com/python/)

[Stack Overflow](https://stackoverflow.com/)
