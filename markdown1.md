# Exploratory Data Analysis of A Disney Dataset

```{figure} python-course-logo.png
---
height: 300px
name: python-logo
---
Python Course Logo!
```
This project was completed as the final project for my python for data science course. Logo source: [UBC Python for Data Science Course webpage](https://prog-learn.mds.ubc.ca/). To present this project on the website and to fulfill my toolbox course project requiremnts, this Jupyter-book is created.

```{margin} **Did you know?**
Disney+ cannot be streamed on TVs that do not come with Disney+ app pre-installed! Bummer!
```


## Dataset Description

```{figure} The_Walt_Disney_Company_Logo.png
---
height: 150px
name: disney-logo
---
This dataset focuses on Disney. [Wikipedia source](https://en.wikipedia.org/wiki/Disney_logo)
```

The dataset has 5 tables, all accessed from [a Disney project on character success](https://data.world/kgarrett/disney-character-success-00-16). Below, information in quotes were taken directly from [this project's analysis report](https://data.world/kgarrett/disney-character-success-00-16/workspace/file?filename=DisneyReport.pdf), {cite:p}`Gar18`. 

- `NOT USED FOR ANALYSIS` **disney-characters.csv**:'provides a list of Disney animated movies and the hero/villain character names in each movie.' It has these columns: 'movie_title', 'release_date', 'hero', 'villain', and 'song.'
- **disney_movies_total_gross.csv**: 'provides a list of Disney movies, and their genre, gross, and MPAA ratings.' The .csv also includes inflation_adjusted_gross as the release dates span a few decades from 1937 to 2016.
- `NOT USED FOR ANALYSIS` **disney-voice-actors.csv**: 'provides a complete list of Disney characters and their voice actors.' It has three columns: 'character', 'voice-actor', 'movie'.
- **disney-director.csv**: 'provides a list of Disney animated movies and the director of each movie.' Note that only first director was scraped from the source data according to the website. 
- **disney_revenue_1991-2016.csv**: 'This is a Disney financial data chart which contains annual gross revenues by sections (includes studio entertainment, parks and resorts, etc.) from 1991-2016.' Note that the units are in million US dollars. 

```{note}
Limitations of this dataset: This dataset is sourced from various sources, some of which were not indicated clearly on the project website. It also primarily focuses on animated movies of Disney based by the data source, whereas Disney does generate non-animated movies as well.
```

## Question(s) of interests

1. Based on existing data, which section is generating more/less revenue over the years of 1991-2006? Is there a trend? 

2. Based on existing data, on average, have movies become more or less revenue generating over time based on inflation-adjusted gross? Which directors are featured in top 10 G-rated inflation-adjusted gross movies in the last half century (1972 - 2022)? 

:::{seealso}
The analysis in this book utilizes a custom function. The custom function is stored in a .py file and hence cannot be displayed as part of the jupyter book. There is also a test custom function .py file that was used to test functionality of the function. For reference, see below the code cells.
:::

```
def custom_filter(colA, valueA, colB, df, N):
    import pandas as pd

    filtered_df = df[df[colA] == valueA]
    new_df = filtered_df.sort_values(by=colB, ascending=False).head(N)

    return new_df
```

```
def test_custom_filter():
    d = {
        "valueA": ["category1", "category1", "category1", "category1", "category2"],
        "valueB": [2, 3, 4, 5, 6],
        "valueC": ["a", "b", "c", "d", "e"],
        }
    df = pd.DataFrame(data=d)
    test = custom_filter("valueA", "category1", "valueB", df, 3)
    
    assert test.shape ==(3, 3), "returned dataframe shape not correct"
    assert test.groupby("valueA").ngroups ==1, 'not filtering correctly"
```


:::{seealso}
One of the columns utilized in the dataset is **inflation adjusted gross**. The dataset does not have any details on how they arrived at those numbers. I wanted to look up the formula commonly used for inflation adjustment just for context. Based on this [source](https://timeseriesreasoning.com/contents/inflation-adjustment/) {cite:p}`Sac21`, below are the equations re-produced based on the source, that can be used to adjust for example, income, by inflation, as well as how the index value (in this case CPI) is calculated.
:::


```{math}
:label: inflation-adjustment
  Inflation~adjusted~value = \frac {Actual~Value}{Index~Value}\times 100
```

```{math}
:label: index-calc
  Value~of~index~in~some~time~period = \frac {Price~of~market~basket~in~time~period}{Price~of~market~basket~in~base~period}\times {index~value~in~base~period}
```
