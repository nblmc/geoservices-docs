[](guide.md "yes")


# How to find and use US census data

By the end of this tutorial, you will have learned:

- How to search for and download census data compatible with mapping
- How to make sense of and use the data you have downloaded
- Some important considerations when working with demographic data in a mapping context

When looking for US census data with the goal of making a map, we recommend using the data portal maintained by the Minnesota Population Center, **NHGIS (The National Historic GIS)**. This data portal has many advantages over official census products like American Fact Finder. It has been designed specifically for use with mapping, the statistical demographic data available via NHGIS is formatted to make joining with geography files simple, and it includes historical boundary files for every census year, beginning with 1790.

1. To start accessing this data, visit [nhgis.org](https://nhgis.org/ "nhgis.org").

2. Choose the **Start Here: Get Data** button in the center of the page, or the **Select Data** option in the left-hand menu. 

The NHGIS portal is formatted like an online shopping cart. You will find the data you are interested in by selecting filters for the data you are interested in, and once it has been narrowed down, adding those datasets to your "cart" and checking out, i.e. downloading the data. 

You will want to use at least the top 3 filters, "Geographic Levels," "Years," and "Topics" to narrow down your data.

In this tutorial, we will be looking for the most recent youth population data available for Boston.

Let's start with the filter "Topics". 

!> 1. Select Topics from the filter menu. 

![topics](/media/gif/topics.gif)

!> 2. We are interested in age, so select **Age** under **Core Demographics**.

You will notice over ten thousand results appear, sorted chronologically beginning with data from 1790. We will need to apply some more filters to get the recent data we are looking for. 

!> 3. Select the filter **Years**. 

The reason we selected our topic first, is because NGHIS will dim out unavailable options in subsequent filters, based on the category of data you are looking for. For example, if we wanted to make a map about American slavery, and had selected that as our first topic, we would only be able to further narrow down our data to decennial years between 1790 and 1860, when censuses included information about slavery. 

Age, being a very standard "core" demographic that has been collected pretty much from the first census up until now, will be included in almost every census.

Now would be a good time to talk about the difference between the total count decennial census and the rolling, continual sample data constantly being collected called the American Community Survey.

The United States Census Bureau attempts to collect as complete a total population count as possible every ten years, and has done so since 1790. Because we are so close at the time this guide was written (February 2020) to our next full count, it means the data from our last total count (2010) is pretty outdated by now.

In the decennial censuses, only a handful of core demographic questions are asked, and they are asked of every person living in the United States. Conversely, more detailed, long-form data is being constantly collected by the Census Bureau, gathered about **sample populations**. This is the American Community Survey. Some pros to the ACS are that the data is much more recent and frequent than the decennial censuses, and more detailed *kinds* of data are collected. A major con is that because the data is sample data, it is less reliable than the full decennial counts, and sometimes has significantly high margins of error.

!> 4. Select the most recent year available, **2018**. You could also select the five-year range, **2014-2018**. Click submit.

The final filter we wish to use is the "Geographic Levels" filter. This will determine the geographic unit by which we will break down our statistical information. For example, if we were to select "State" we could make a map of the number of under-18 population for each state in the United States.

When working with city data, a good geographic unit to select is census tract. County-level data would not be specific enough to give you a meaningful understanding of geographic patterns. For core demographic data, block-level information is often available, and is even more specific than census tracts, but this option is not always available for more specific, or non-core demographic data.

!> 5. Under Geographic Levels, select **Census Tract**

Our results have now been filtered down to a few hundred, rather than ten thousand!










*For questions related to geospatial data and mapping, please visit https://www.leventhalmap.org/research/geospatial-data/*
