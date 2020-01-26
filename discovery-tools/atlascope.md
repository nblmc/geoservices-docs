## Welcome

Welcome to the user guide for [Atlascope](https://atlascope.leventhalmap.org/ "Atlascope"), a web app for browsing and researching with the rich collection of urban atlases held at the Boston Public Library. 


<iframe width="400" height="550" src="https://atlascope.leventhalmap.org/#view:embed$base:001$overlay:39999059011690$zoom:18.00$center:-7912348.885480463,5213458.735922582$mode:glass$pos:145"></iframe>


For researching urban history in the US, **urban atlases**, like the ones produced for fire insurance surveys, are some of the most important resources. But because these atlases are physically clumsy, and broken up page-by-page into areas covering usually only a few city blocks, it’s not always easy to find what you’re looking for, and even more difficult to compare across time.

Thanks to a grant from the [Council on Library and Information Resources](https://www.clir.org/ "CLIR"), the Leventhal Map & Education Center has been taking our urban atlases and transforming them into continuous, zoomable web layers. 

Doing so takes a ton of hand labor identifying control points and mosaicing the pages together at their boundaries, a process which our interns have been taking on with great zeal. (If you work with these resources and are looking to replicate this process, please find our [Create Mosaics How-to Guide](http://geoservices.leventhalmap.org/#/how-to/create-mosaics "Create Mosaics How-to Guide") )

On top of this GIS work, we’ve built a brand new web interface which automatically pulls up the atlases which cover an area you’re interested in. Atlascope allows you to compare historic atlases to one another and to modern maps, and then find the original items in the library collections. It’s an amazing resource for anyone interested in exploring how Boston has changed over time.

This guide will walk through some of the ways Atlascope can help you use the urban atlas collection at the Boston Public Library.


## Credits {docsify-ignore}

Atlascope was developed at the Leventhal Map & Education Center at the Boston Public Library by Garrett Dash Nelson and Belle Lipton. Atlas layers were prepared by a team of interns including Ian Donnelly, Hanaan Yazdi, Abby Duker, Rachel Mead, Luwei Chen, Brian Kominick, Madison Bastress, Liz Kellam, Victoria Mak and Samantha Carr.

Digitization and preparation of atlas layers was made possible by the [Council on Library and Information Resources.](https://www.clir.org/ "CLIR")

If you use these maps in your work, teaching, or publication, please cite Atlascope Boston, Norman B. Leventhal Map & Education Center at the Boston Public Library, together with the bibliographic information for the map(s) used, which is available in the "About this Map" tab from the map window view.

Interested in creating an Atlascope for your own city or library collection? Contact us for more information.


## Search by location


### Dynamic menus {docsify-ignore}

Each historical atlas included in the project has a different geographic coverage. This is because the atlases were created for different towns and areas, at a time when the urban landscape was developing rapidly. For these reasons, no two atlases in our collection have exactly the same geographic extent.


When using Atlascope, you can pan and zoom around the map, and Atlascope will automatically find all historical layers that are available for that particular location.

!> **As you move** around the map, the dropdown **menus** with available atlas layers **will change** and update to reflect what is available for that area.

![menu](/media/gifs/menu.gif)


As you move out of the range of one atlas, the app will automatically suggest the oldest atlas layer available for the new map location.


## Find me 

Atlascope was designed to be used on-the-go!

From the Atlascope home screen, select `Find me` to find your current location and return historical atlas layers available for that location.

![available](/media/img/find-me.png)


If you want the app to follow your path as you meander through Boston, select `Follow` in response to the prompt "Do you want the map to move with you?"

The `Find me` + `Follow` combination is fun to try on foot or on the MBTA!

If you would like to find your location initially as a point of reference, and then turn off all subsequent tracking, select `No` to when asked if you want the map to move with you.

> You will need to enable location services on your device for the Find me tool to work. The Leventhal Map & Education Center does not record any of the location data; location services are required only to enable the Find me tool to work as you explore the city.


## All available layers

To access a list of all atlases available in the app, please follow the steps below.

!> **Zoom out on the map** by using your computer cursor, or by pinching the screen on your touch device. Eventually, the tiles will disappear, and polygon shapes representing each available atlas layer will appear.

To return to a historical map layer, you have two options.

1). Using the map interface to zoom back in on an area.

![zoom all](/media/gifs/zoom-all.gif)

2). From the polygon extent interface, expanding the "Choose an atlas..." menu to find a list of all available app layers.

Selecting one of the list options will turn tiles on for that layer.

![list](/media/gifs/list.gif)

Atlascope includes a selection of the town, county and urban atlases available at the Boston Public Library. To learn more about the full research collection, please find the [All urban atlases @ the BPL guide.](https://geoservices.leventhalmap.org/docs/#/atlascope/using/all-atlases "All atlases @ BPL")


## Search by address

There are two ways to search for atlases using a modern day address.

> **From the home screen**, select "Search places"

![search home](/media/img/address.png)

> **From the app menu controls**, select "Search places"

![search menu](/media/img/menu-search.png)

You can search for either modern street addresses or the names of businesses. If the search recognizes your query, you will see a suggested result.

![search business](/media/img/business.png)

Selecting a suggested result will bring you to that location on the map, and turn on atlas tiles for that location.

![search results](/media/img/beehive.png)


## Comparison tools

There are a few different tools available in the app to compare historical atlases.

You can control the overlay appearance by switching between Glass, Swipe, or Opacity modes.

### Glass 

The default overlay mode in the app is the `Glass mode`, named so for its resemblance to a spyglass.

This mode provides a neat way to "peer through" the baselayer to whichever atlas is selected inside the Glass view.

We tend to think of `Glass mode` as a rather convenient way to use Atlascope, because of the ability to increase or decrease the size of the glass, allowing total customization of the comparison between the baselayer and the glass map.

![glass](/media/gifs/glass.gif)

Glass mode can be activated at any time by selecting "Glass" from the app menu controls.

![glass](/media/img/glass.png)

### Swipe 

Another mode available is `Swipe mode`.

You can change the direction of the swipe by toggling between `Swipe Y` and `Swipe X` in the app menu controls.

![swipe](/media/gifs/swipe.gif)



### Opacity 

The final available overlay mode is `Opacity mode`.

`Opacity mode` can be activated at any time by selecting `Opacity` in the menu layer controls.

In addition to using the range slider to gradually increase or decrease opacity, try selecting "0" or "100" on either end of the slider to quickly toggle the overlay off and on.

![opacity](/media/gifs/opacity.gif)



## Change over time 


Try setting both the base and overlay layers to historic atlases. What comparisons can you make that show how the city has changed?

Let's compare a few blocks in South Boston between 1885 and 1891...

In `Glass mode`

![compare glass](/media/gifs/compare-glass.gif)

In `Swipe mode`

![compare swipe](/media/gifs/compare-swipe.gif)

In `Opacity mode`

![compare opacity](/media/gifs/compare-opacity.gif)




## Sharing

To share a link to the whole app, or a specific view/location, following these steps:

1. Click the Share button in the upper-right hand corner
![share](/media/img/share.png)

2. Select the appropriate share option <br><br>
![share](/media/img/share-options.png)


## Get the maps

While using mosaiced atlas layers inside the Atlascope app is an intuitive way to access the materials, we understand there will certainly be cases where you wish to access high-resolution scans of individual atlas plates, and thus will need to be able to locate these unique items in our [digital collections](https://collections.leventhalmap.org/ "Digital collections").

Or maybe, you even wish to visit the Map Center, and [research](https://www.leventhalmap.org/research/ "Research @ LMEC") with particular atlas pages in person!

For these reasons, Atlascope works symbiotically with our traditional library interfaces, specifically our digital collections and collection-level research guides for the historical urban atlas collection.

In this guide you will learn how to use Atlascope to quickly find atlas plates in the digital collections, download high-resolution images of the maps, and grab the map's citations.

### Steps {docsify-ignore}

1). Use the location or address-based search to find a location.

2). Zoom in close to the area of interest.

3). Use the menus to select the appropriate atlas year.

4). From the app layer controls, select "About this map"

![About this map](/media/img/about-this-map.png)

Here, you will find bibliographic information about the volume, and will be presented with options for finding this resource in the library collections.

![collections options](/media/img/lib-options.png)

**View plate boundaries and atlas extent** will take you to a page with only the layer for that atlas, and an outline showing each page in the atlas. Each blue/green shape corresponds with one page in that historical book, which is available to research with in person at the Map Center. 

![extent](/media/img/extent.png)

When you click on a shape, a popup will tell you more biliographic information, including the collections identifier # for that page in our digital collections, and a link to the item.

![popup](/media/img/popup.png)



**View list of plates in the Digital Collections** will bring you to a query in the digital collections returning all results for plates associated with that volume's call number. This will essentially be a gallery of thumbnails. You will still need to page through the results to find the plate with the location of interest.

*Hint:* This is a great way to find the index page for any atlas, which includes a symbology key. Each publisher uses different colors and markings to indicated different factors, so the index page legend can be helpful, and is available in the digital collections.


**Find this plate in the Digital Collections** will bring you to a page with only that atlas layer again, but this time, zoomed in on the area you had been engaging with in the app.

Click on the exact location you are looking for, and from the resulting popup, click "View in Digital Collections"

![find-this-plate](/media/gifs/dc.gif)



- To download a high-resolution scan, navigate to `Downloads` and select `Master (full resolution, uncompressed)`

![download](/media/img/download.png)

- To cite this plate, select "Cite". A citation will be automatically generated.

![cite image 1](/media/img/cite1.png)

![cite image 2](/media/img/cite2.png)




## All atlases @ BPL


While Atlascope includes an amazing number of atlases from the BPL collections covering Boston and surrounding towns, it does not include a significant portion of atlases available for research at the BPL.

**Atlases not included in Atlascope**

- Atlases outside of Boston Proper for most towns in Massachusetts - *coming soon!*

- Atlases published after 1923 where rights are still retained by the copyright owner. This includes most of the twentieth-century Sanborns.

Though you cannot access these important archives in the app or digital collections quite yet, you **_can_** research with them in person. Here's how:

1). Submit a reference request using our [research form.](https://www.leventhalmap.org/research/ "Research @ LMEC")

2). Use our libguides to find a complete record of what's available.


### Using the libguides {docsify-ignore}

1). Navigate to the [Historical Urban Atlases of Boston Libguide.](https://guides.bpl.org/urban-atlases "Urban Atlas Libguide")


2). To find a list of citations organized by neighborhood and chronology, select `List of Urban Atlases`.


3). To find all Boston urban atlases available for research **by location** click the `Find by Map` tab on the libguides. Atlases are grouped by neighborhood. Selecting an atlas from one of the neighborhood maps will tell you if that particular publisher/year has been added to Atlascope yet. 

If it *has* we recommend using Atlascope to explore, as it is easier. If it has not yet been added, selecting that layer will prompt a boundary layer to appear, so you can still get information about a plate, or find a specific location in the digital collections.

![libguides](/media/gifs/libguides.gif)





If you are looking for towns outside of Boston, from the guides.bpl.org/urban-atlases page, navigate to **Related Resources** tab on the left, select `Historical Urban Atlases of Massachusetts Towns @ the BPL`.

![Towns](/media/img/towns.png)

This will bring you to a complete listing of historical town atlases available for research at the BPL. They are organized by County.

For questions related to researching with the BPL holdings, please do not hesitate to get in touch via our [research form](https://www.leventhalmap.org/research/ "Research @ LMEC") or via email at reference@leventhalmap.org. 


## Mosaic links

We think one of the coolest aspects of creating high-resolution tiled mosaic layers of each atlas is our ability to share them with you.

This section of the guide will give instructions on how to bring in the mosaic of any atlas in Atlascope to your own GIS project. 


The tiles for each volume are accessible by selecting `About this map` and then copying the link under `XYZ Tile Endpoint`

![tiles](/media/img/tiles.png)

This link can be brought into any geospatial software -- desktop software like ArcMap, ArcGIS Pro, and QGIS, cloud mapping platforms like ArcGIS Online, Carto and Google Maps, and you can even use them to build your own Javascript web apps, like we did with Atlascope!

For any questions centered on using these tiles as layers in your own project, or any questions related to geospatial data and mapping, please do not hesitate to reach out to us via our [geospatial research form.](https://leventhalmap.org/research/geospatial-data "Geospatial Research @ LMEC")

