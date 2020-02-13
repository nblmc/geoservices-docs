[](guide.md "yes")


# How to find and use US census data

## Overview
By the end of this tutorial, you will have learned:

- How to search for and download census data compatible with mapping
- How to make sense of and use the data you have downloaded
- Some important considerations when working with demographic data in a mapping context

When looking for US census data with the goal of making a map, we recommend using the data portal maintained by the Minnesota Population Center, **NHGIS (The National Historic GIS)**. This data portal has many advantages over official census products like American Fact Finder. It has been designed specifically for use with mapping, the statistical demographic data available via NHGIS is formatted to make joining with geography files simple, and it includes historical boundary files for every census year, beginning with 1790.

!>  To start accessing this data, visit [nhgis.org](https://nhgis.org/ "nhgis.org").

!>  Choose the **Start Here: Get Data** button in the center of the page, or the **Select Data** option in the left-hand menu. 

The NHGIS portal is formatted like an online shopping cart. You will narrow down all available data by applying filters, and then add your desired datasets to your "cart" and "check them out", i.e. download the data. 

You will want to use at least the top 3 filters, "Geographic Levels," "Years," and "Topics" to narrow down your data. The next section of this tutorial will describe how to use these filters.

## Data Filters
In this tutorial, we will be looking for the most recent youth population data available for Boston.

Let's start with the filter "Topics". 

!>  Select Topics from the filter menu. 

![topics](/media/gif/topics.gif)

!>  We are interested in age, so select **Age** under **Core Demographics**.

You will notice over ten thousand results appear, sorted chronologically beginning with data from 1790. We will need to apply some more filters to get the recent data we are looking for. 

!> 3. Select the filter **Years**. 

The reason we selected our topic first, is because NGHIS will dim out unavailable options in subsequent filters, based on the category of data you are looking for. For example, if we wanted to make a map about American slavery, and had selected that as our first topic, we would only be able to further narrow down our data to decennial years between 1790 and 1860, when censuses included information about slavery. 

Age, being a very standard "core" demographic that has been collected pretty much from the first census up until now, will be included in almost every census.

Now would be a good time to talk about the difference between the total count decennial census and the rolling, continual sample data constantly being collected called the American Community Survey.

The United States Census Bureau attempts to collect as complete a total population count as possible every ten years, and has done so since 1790. Because we are so close at the time this guide was written (February 2020) to our next full count, it means the data from our last total count (2010) is pretty outdated by now.

In the every-ten-year censuses, only a handful of core demographic questions are asked, and they are asked of every person living in the United States. Conversely, more detailed, long-form data is being constantly collected by the Census Bureau, gathered about **sample populations**. This is the American Community Survey. Some pros to the ACS are that the data is much more recent and frequent than the decennial censuses, and more detailed *kinds* of data are collected. A major con is that because the data is sample data, it is somewhat less reliable than the full decennial counts, and sometimes has significantly high margins of error. 

!>  Select the most recent year available, **2018**. You could also select the five-year range, **2014-2018**. Click submit.

The final filter we wish to use is the "Geographic Levels" filter. This will determine the geographic unit by which we will aggregate our statistical information. The Census Bureau makes data available in the aggregate, as opposed to providing information about individuals. For example, instead of downloading a spreadsheet where every row represents one person, and contains information about that person, we have access to counts or tallies of people who live in certain areas. For example, if we were to select "State" from the Geographic Levels filter, we would be downloading a spreadsheet where every row represents one US state, and contains information about the number of under-18 population in that state. 


We are mapping Boston, so a good geographic unit to select is census tract. County-level data would not be specific enough to give us a meaningful understanding of geographic patterns. Most modern day data is available at the tract level, which is more specific than state or county. Some, but not all data is even available at the block-level!


An important factor to keep in mind when aggregating statistical figures to a geographic area is the often arbitrary and sometimes intentional ways borders are defined, and how those choices can affect how we read the geographic distribution. This problem is called the Modifiable Areal Unit Problem (MAUP), and is demonstrated in this graphic below:

![maup](/media/img/maup.png)


!>  Under Geographic Levels, select **Census Tract**

Our results have now been filtered down to a few hundred, rather than ten thousand. You will notice there are lots of different ways age demographic data is organized and categorized. The dataset we are looking for doesn't appear in our results until page 5.


!>  Click through to page 5 of the results and find dataset "Population Under 18 Years by Age". 


!>  Under Classifications, click **Age(8)**






*For questions related to geospatial data and mapping, please visit https://www.leventhalmap.org/research/geospatial-data/*
