# Conclusions

## On Question 1

The analysis on question 1 talked about the limitations of the dataset pulled from this other project. Further more, see note below on how NaN was handled.

After looking at data, Disney Interactive column was dropped due to more than half of the column being NaN value - it represents a smaller sector of the total income anyways. Any rows with NaN values in other columns are dropped before generating the plot to visualize revenues over-time. A melt function was used so all the discussed sections can be presented on the same plot for visual comparison. 

I was slightly surprised to see the Studio Entertainment plateauing, while the other sections more or less increasing over time. To my understanding, the animated movie data presented in the rest of the datasheet falls under this category. Therefore, it natually raise the second question in this project - the question of how the movie perform in gross revenues over time, and the expectations would be they did not perform as well. I also had to raise this second question due to me not finding a portion of the first question that can be put into a meaningful function.

```{margin} **Did you know?**
Walter Disney just released their Quarter 4 earning for FY2022 - reporting a 23% increase in revenues. See [source from their website](https://thewaltdisneycompany.com/app/uploads/2022/11/q4-fy22-earnings.pdf). 
```

## On Question 2

As mentioned previously, the expectation is movies are generating less revenue over time for Disney.  

After visualizing the movies' average gross by year, as well as the number of movies produced each year, it shows that: 1937 with movie Snow White and the Seven Dwarfs, is so high in gross that it may make the downward trend more stiff than it could have been without it. It appears that there were some major hits in box office for earlier (pre-1970) fims, after the 1970s, despite increased number of movies produced each year, the average gross for movies have come down. Since 2010, despite decreased number of movies compared to the 1990s, there has been a slight upward trend despite the average box office remain low. This contradicts my expection that newer movies would have been more revenue generating. 

Based on the findings, for the revenue-generating top director question, I set the last half century (1972-2022) as the time frame as I feel there's more movies produced for analysis, as well as there are less particularly outstanding data points in this range (no box office as high as Snow White and the Seven Dwarfs, for example), so this time frame is more comparable.

I created a custom filter for the data filtering and loc, as I feel many other slightly different questions could have been raised with the merged data, e.g. which directors generated the top N movies, in a particular or all MPAA ratings and/or under a specific genre. The question itself though, is to look for top 10 directors for G-rated category.

```{Note}
To my future self: Data science apparently involve more math than I'm currently comfortable with. May be a good idea to take up [a course on math](https://www.coursera.org/learn/datasciencemathskills). 
```

For example, some of the math concepts that may be covered by this coursera course according to its syllabus:

```{math}
:label: bayes-theorem
  P(A|B) = \frac {P(B|A)\cdot P(A)}{P(B)}
```

[Formula source](https://en.wikipedia.org/wiki/Bayes'_theorem)

```{Note}
To my future self: Coding is another apparent barrier to my ability to wrangle data, visual presentation, and present data, so might be a good idea signing up for [a python course](https://extendedlearning.ubc.ca/programs/introduction-systematic-program-design-python). 
```

## End of Jupyter Book
This page also concludes the end of this Jupyter Book, as final project for the Data Science Toolbox course. 

```{figure} toolbox_logo.PNG
---
height: 250px
name: toolbox_logo
---
Toolbox Course Logo.
```
[Logo source](https://toolbox-learn.mds.ubc.ca/en/).

```{figure} fireworks.jpeg
---
height: 300px
name: fireworks
---
Yay done!!.
```
[Logo source](https://www.porthope.ca/en/living-here/fireworks.aspx).

