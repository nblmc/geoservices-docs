## Picking a service

When looking for US census data with the goal of making a map, we recommend using the data portal maintained by the Minnesota Population Center, NHGIS (The National Historic GIS). This data portal has many advantages over official census products like American Fact Finder. It has been designed specifically for use with mapping. The statistical demographic data available via NHGIS is formatted to make joining with geography files simple, by including a field "GISJOIN" in every file. It also includes historical boundary files for every census year, beginning with 1790, so that if you want to make a map of how areas have changed demographically over time, you can easily find boundaries complementary to the historic statistical information.

## Data facets

The NHGIS portal is formatted like an online shopping cart. You will narrow down all available data by applying facets, and then add your desired datasets to your "cart" and "check them out", i.e. download the data. 

You will want to use at least the top 3 facets, "Geographic Levels," "Years," and "Topics" to narrow it down.


After you have selected one facet, NGHIS will dim out any unavailable options for the other facets, based on other categories you have selected. For example, if we were interested in making a map about populations of enslaved people in the early 1800s using census data, and had selected "slavery" as our first **topic** facet, when we went to choose from **year** options, we would only be able to select data from narrow census years between 1790 and 1860, when the Census Bureau collected information about the United States' enslaved population. 



## Years 


An important factor to be aware of is the difference between the total count decennial census and the rolling, continual sample data constantly being collected called the American Community Survey.

The United States Census Bureau attempts to collect as complete a total population count as possible every ten years, and has done so since 1790. Because we are so close at the time this guide was written (Spring 2020) to our next full count, it means the data from our last total count (2010) is pretty outdated by now.

In the every-ten-year censuses, only a handful of core demographic questions are asked, and they are theoretically asked of every person living in the United States. You may notice how short the census are from when you filled out your own 2020 census. It should have only taken about 5 - 10 minutes. 

The census **also** collections much more detailed, long-form data. This data, however, is not gathered about every single person, rather, it is gathered about **sample populations**. This is called the American Community Survey. Some pros to the ACS are that the data are much more recent and frequent than the decennial censuses, and more detailed questions are asked of respondents. A major con is that because the data are **sample data**, they are less reliable than the full decennial counts, sometimes having significantly high [margins of error](https://www.statisticssolutions.com/how-does-margin-of-error-work/ "margins of error"). 

## Aggregation 

The final filter we wish to use is the "Geographic Levels" filter. This will determine the geographic unit by which we will aggregate our statistical information. The Census Bureau makes data available in the aggregate, as opposed to providing information about individuals. This is good, because we don't want to put people's privacy at risk by releasing personal information about them. Instead, the census shares people's data by grouping the results into one number for each area.

By using the "Geographic Levels" filter, we can pick how big or small we want the summary areas on our map to be. Data is available all the way at the broad state level, which you would pick if you wanted to make a map of the number of people for every state, all the way down to a small city block.

What does this look like when we download the data? Instead of downloading a spreadsheet where every row represents one person, and contains information about that person, we can download the count or tally of people who live in a geographic unit. It's up to us to decide which geographic unit we want for our map. For example, if we were to select "State" from the Geographic Levels filter, we would be downloading a spreadsheet where every row represents one US state, and contains an under-18 summarized number for that state.


In our activity, we want to show demographic makeup of Boston, so a good geographic unit to select would be census tract. County-level data would not be specific enough to give us a meaningful understanding of geographic patterns, but census tracts are smaller than counties, so using tracts would give us that level of precision. Most modern day data are available at the tract level, so it is a reliable unit to pick, if you are looking for specific data. Blocks are even more specific, but not all data is available at that level.

[🎠 add pics of each geographic unit for Boston ]


Even though its important to protect people's privacy, any time we summarize individual data points into groups using geography, problems arise. Most of these problems are tied to the issues inherent in the sometimes arbitrary and sometimes intentional ways borders have been and continue to be defined by **people**. How those choices have been made and continue to be made affects the ways we read geographic distribution on maps. This very common problem is called the Modifiable Areal Unit Problem (MAUP), and is demonstrated in this graphic below:

![maup](https://geoservices.leventhalmap.org/docs/media/img/maup.png)

This graphic depicts how, depending on where the boundary line is drawn, singular occurrences of a phenomenon are grouped together differently, changing our visual reading of any given area's percentage or proportion of the phenomenon at hand. 

Being aware of issues like margins of error and MAUP make us more critical consumers and more effective and ethical creators of visual graphics.


