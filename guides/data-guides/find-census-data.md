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

!>  We are interested in age, so select **Age** under **Core Demographics**, by clicking the green plus sign. 

You will notice over ten thousand results appear, sorted chronologically beginning with data from 1790. We will need to apply some more filters to get the recent data we are looking for. 

!> 3. Select the filter **Years**. 

The reason we selected our topic first, is because NGHIS will dim out unavailable options in subsequent filters, based on the category of data you are looking for. For example, if we wanted to make a map about American slavery, and had selected that as our first topic, we would only be able to further narrow down our data to decennial years between 1790 and 1860, when the Census Bureau collected information about the United States' enslaved population. 

Age, being a "core" demographic that has been gathered from the first census up present day, can be found in every census year.

Another factor to be aware of is the difference between the total count decennial census and the rolling, continual sample data constantly being collected called the American Community Survey.

The United States Census Bureau attempts to collect as complete a total population count as possible every ten years, and has done so since 1790. Because we are so close at the time this guide was written (early Spring 2020) to our next full count, it means the data from our last total count (2010) is pretty outdated by now.

In the every-ten-year censuses, only a handful of core demographic questions are asked, and they are theoretically asked of every person living in the United States. Conversely, more detailed, long-form data is being constantly collected by the Census Bureau, gathered about **sample populations**. This is the American Community Survey. Some pros to the ACS are that the data are much more recent and frequent than the decennial censuses, and more detailed questions are asked of respondents. A major con is that because the data are sample data, they are less reliable than the full decennial counts, sometimes having significantly high margins of error. 

!>  Select the most recent year available, **2018**. You could also select the five-year range, **2014-2018**. Click submit.

The final filter we wish to use is the "Geographic Levels" filter. This will determine the geographic unit by which we will aggregate our statistical information. The Census Bureau makes data available in the aggregate, as opposed to providing information about individuals. For example, instead of downloading a spreadsheet where every row represents one person, and contains information about that person, we have access to counts or tallies of people who live in certain areas. For example, if we were to select "State" from the Geographic Levels filter, we would be downloading a spreadsheet where every row represents one US state, and contains counts about the number of under-18 population in that state. 


In this example, we are mapping Boston, so a good geographic unit to select is census tract. County-level data would not be specific enough to give us a meaningful understanding of geographic patterns. Most modern day data are available at the tract level, which is more specific than state or county. Some, but not all data is even available at the block-level!


An important factor to keep in mind when aggregating statistical figures to a geographic area is the often arbitrary and sometimes intentional ways borders are defined, and how those choices can affect how we read the geographic distribution. This problem is called the Modifiable Areal Unit Problem (MAUP), and is demonstrated in this graphic below:

![maup](/media/img/maup.png)

This graphic depicts how, depending on where the boundary line is drawn, singular occurrences of a phenomenon are grouped together differently, changing our visual reading of any given area's percentage or proportion of the phenomenon at hand. 

Being aware of issues like margins of error and MAUP make us more critical consumers and more effective and ethical creators of visual graphics.

!>  Under Geographic Levels, select **Census Tract**

Our results have now been filtered down to a few hundred, rather than ten thousand. You will notice there are lots of different ways age demographic data is organized and categorized. The dataset we are looking for doesn't appear in our results until page 5.


!>  Click through to page 5 of the results and find dataset "Population Under 18 Years by Age". 


You will need to use the datasets' title descriptions and classification breakdowns to determine which datasets are of most use to your project.

In this case, we were looking for population data broken into different age brackets, because we were interested in evaluating the impact of library locations on different school-age populations.

You can learn more about each dataset's classfication by clicking on the variable name under the column "Classifications"

!>  Under Classifications, click **Age(8)**

![age](/media/img/age.png)


Upon clicking on the age variable's classification breakdown, the data appears to be categorized into age brackets: under 3 years, 3-4 years, 5 years, 6-8 years, 9-11 years, and so on. This looks promising. Let's download this dataset.


!>  Add the dataset to your cart by clicking the green plus sign to the left of the data listing

Your "cart" in the upper right-hand corner of the webpage will now reflect that you have added one source table.


![cart](/media/img/cart.png)

Remember, whatever statistical demographic information we are "checking out" is just that -- a table of figures. In order to connect this information with geography, we will need to also download a geography file at the proper unit (tract, county, state, etc.), and combine the two together, after we have downloaded them. 

![no-gis](/media/img/no-gis.png)


Normally, GIS files at the geographic unit we have selected will appear under the tab "GIS Files". Right now, it is telling us that there are 0 GIS Files.

The reason no GIS files are appearing is because we have selected a non-decennial year, 2018. While American Community Survey (ACS) data is being constantly collected, they are aggregated to the most recent decennial geography, which is only updated every ten years. That means we will need to change our **year** filter to 2010 in order to obtain a correct census tract file to join our statistical information with. 

!>  Change the **Years** filter to **2010**

The GIS Files tab should now have two listings

![years](/media/img/years.png)


!>  Add the first record to your cart, the one that uses the 2010 TIGER/Line as its basis

Your cart should now list 1 Source Table and 1 GIS File

![checkout cart](/media/img/cart2.png)

!>  Inside the data cart, select **Continue**

You will be brought to a page to review your selection. 

!>  Select **Continue** again

On the final Review and Submit page, observe the options. The defaults (comma delimited and data all in one spreadsheet) are OK for our purposes.

!>  Select **Submit**

Here you will be prompted to create a free account. This is used to manage your download history. 

!>  Create an account 

Once you have created your account and the data request has been processed (it takes a little under five minutes), you will receive an email that your data is ready to download. You can also refresh the Extracts History page until your extract is ready. 

You will know it is done when **tables** and **gis** appear with a file size. 

![extract](/media/img/extract.png)

!>  Click on each of the files, **tables** and **gis** separately to initiate the download

The data will be downloaded as zip files.

!>  From your **Downloads** folder, right-click each of the files and "unzip" or "extract" it

The "shape" or geography files are often double-zipped. You will need to unzip this file one more time before being able to use it.

!>  Double-click the newly-extracted "nhgis0020_shape" folder. There will be another zipped folder inside, titled "nhgis0020_shapefile_tl2010_us_tract_2010". Right-click > extract or unzip this folder

## Data Codebook

Let's take a look at the data we have downloaded, and clean it up a bit before bringing it into GIS software. 

In your Downloads folder, there should be a folder that ends with "_csv". Inside this folder there should be a .csv file, and a .txt file. 

!> Open the .csv file 

Take a look at the data. Lots of fields will be self-evident, like the State and County names. There will be lots of blank fields as well. Let's delete some blank fields to make working with the data a little easier.

!> Delete all the empty columns: "REGIONA", "DIVISIONA", "COUSUBA", "PLACEA", and the big gap starting with "CONCITA" up to "BTTRA"

The remaining data has many field names that don't make a lot of intuitive sense, beginning with "AKA2E001". What does this field represent?

When you find statistical or geospatial data online in open data portals, if the data is any good, it will be accompanied by what is referred to variously as "metadata," "documentation" or, in this case "the data codebook." Essentially these files contain data *about* the data (that's why it's called *meta*-data)

Some common information included in metadata or documentation are:
- what organization collected the data
- what organization published the data
- what processing steps were performed on the data
- what year the data was collected or published
- a field name dictionary or de-coder

You can think of these files as very detailed citations, like in a book or academic paper. If you find data online and they do not have accompanying metadata that you can inspect to trace back the source's authority, it would be reasonable to be skeptical of that data. 

Luckily, NHGIS is a high-quality data provider, and includes extensive documentation with every data extract, in the format of .txt data codebooks.


!> Double-click the downloaded file ending with "_codebook.txt" to open it. 


## GIS Join
To work with this data, we will use QGIS, a free & open geospatial software. 

!> Open QGIS. If you do not already have QGIS, download it [here](https://qgis.org/en/site/forusers/download.html "QGIS download")


*For questions related to geospatial data and mapping, please visit https://www.leventhalmap.org/research/gis/*
