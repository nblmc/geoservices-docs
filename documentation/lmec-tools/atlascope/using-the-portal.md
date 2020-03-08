## Welcome

Welcome to the user guide for **Atlascope**, a web app for browsing and researching with the rich collection of urban atlases held at the Boston Public Library. 


<iframe width="400" height="550" src="https://atlascope.leventhalmap.org/#view:embed$base:001$overlay:39999059011690$zoom:18.00$center:-7912348.885480463,5213458.735922582$mode:glass$pos:145"></iframe>

*Embedded above: A Boston Bromley in Atlascope. Try zooming or panning to explore Copley Square in 1938.* 


Urban atlases, like the ones produced for fire insurance or real estate companies like Sanborn and Bromely, are some of the most important resources for researching urban history in the United States. [Many library](https://www.loc.gov/rr/geogmap/sanborn/san4a1.html "Many library") collections hold copies of fire insurance or real estate atlases, and librarians at these repositories can tell you how popular these works are with researchers, genealogists, historians, and those with a focus on urban studies. 

The collection of urban atlases held at the Boston Public Library and cared for by the Leventhal Map & Education Center is one of the most comprehensive and complete collections of fire insurance atlases in existence for the state of Massachusetts. But because these atlases are physically clumsy, and broken up page-by-page into areas covering usually only a few city blocks, it has not always been easy to find the area you are looking for, and even more difficult to compare how an area has changed over the course of time.

**Enter Atlascope!** <br>
Atlascope → https://atlascope.leventhalmap.org/

Thanks to a grant from the Council on Library and Information Resources [[CLIR](https://www.clir.org/ "CLIR")], we have been taking our urban atlases and transforming them into continuous, zoomable web layers. 

Doing so takes a ton of hand labor digitally identifying control points and mosaicing the pages together at their boundaries, a process which our interns have been taking on with great zeal. To learn more about the mosaicing process, check out our [Create Mosaics Guide](http://geoservices.leventhalmap.org/#/how-to/create-mosaics "Create Mosaics").

On top of this GIS work, we’ve built a brand new web interface which automatically pulls up the atlases which cover an area you’re interested in. This discovery interface, Atlascope, allows you to compare historic atlases to one another and to modern maps, and then find the original items in the library collections. It’s an amazing resource for anyone interested in exploring how Boston has changed over time.

The rest of this guide will walk through some of the ways Atlascope can help you use the Boston Public Library's urban atlas collection.


#### Credits {docsify-ignore}

Atlascope was developed at the Leventhal Map & Education Center at the Boston Public Library by Garrett Dash Nelson and Belle Lipton. 

Atlas layers were prepared by a team of interns including Ian Donnelly, Hanaan Yazdi, Abby Duker, Rachel Mead, Luwei Chen, Brian Kominick, Madison Bastress, Liz Kellam, Victoria Mak and Samantha Carr.

Digitization and preparation of atlas layers was made possible by the Council on Library and Information Resources [[CLIR](https://www.clir.org/ "CLIR")].

If you use these maps in your work, teaching, or publication, please cite Atlascope Boston, Norman B. Leventhal Map & Education Center at the Boston Public Library, together with the bibliographic information for the map(s) used, which is available in the "About this Map" tab from the map window view.

Interested in creating an Atlascope for your own city or library collection? Contact us for more information.


## Searching 

There are two main ways to search in Atlascope: 
1. by finding the location on the **map**
2. by typing in an **address**

### map 

Each historical atlas included in Atlascope has a totally different geographic coverage from all the others. This is because the atlases were created separately for different regions, and were published at a time when Boston's urban landscape was developing rapidly. 

![atlases](https://geoservices.leventhalmap.org/docs/media/img/atlases.png)

*Pictured above: Geographic extent snapshot of atlases available in Atlascope*

For these reasons, no two atlases in our collection have identical coverages.

> **As you move** around the map, the dropdown **menus** with available atlas layers **will change** and update to reflect what is available for that area.

![menu](https://geoservices.leventhalmap.org/docs/media/gif/menu.gif)


As you move out of the range of one atlas, the app will automatically suggest the oldest atlas layer available for the new map location.



### address

Here are the steps to search for a modern-day address:

1. When you first open the app, from the "Where do you want to start exploring" home screen, select "Search places"

2. If you are already in the map interface, click "Search places" from the menu



![search menu](https://geoservices.leventhalmap.org/docs/media/img/menu-search.png)

You can search for either modern street addresses or the names of businesses. If the search recognizes your query, a suggested result will appear.

![search business](https://geoservices.leventhalmap.org/docs/media/img/business.png)

Clicking on a suggested result will bring you to that location on the map, and also turn on imagery for that location.




## Find me 

Atlascope was designed to make exploring Boston  history easy and fun. It works well on an phone or tablet, and a "locate me" tool exists to situate yourself in history while you are moving about in the city.

This section of the guide will explain how to enable location services in the app in order to find your current location, and if you wish, have the app track you as you move around.

No location data is collected; this tool exists only so you can easily find where you are and compare what exists in real life to what existed a century ago. You can also choose to ignore this feature, and leave your location services turned off.


> **→** From the Atlascope home screen, select **Find me** to find your current location and return historical atlas layers available for that location. <br> 
>
> **→** If you want the app to follow your path as you meander through Boston, select **Follow** in response to the prompt "Do you want the map to move with you?" <br>
>
> **→** The **Find me** + **Follow** combination is fun to try on foot or on the MBTA! <br>
>
> **→** If you would like to find your location initially as a point of reference, and then turn off all subsequent tracking, select **No** to when asked if you want the map to move with you. 




## Overlaying

Atlascope has three options for overlaying layers: glass, swipe, or opacity modes. 

### glass

The default overlay mode in the app is the `Glass mode`, named so for its resemblance to a spyglass.

This mode provides a neat way to "peer through" the baselayer to whichever atlas is selected inside the Glass view.

We tend to think of `Glass mode` as a rather convenient way to use Atlascope, because of the ability to increase or decrease the size of the glass, allowing for a more fine-tuned comparison between the base and overlay map.

![glass](https://geoservices.leventhalmap.org/docs/media/gif/glass.gif)


### swipe

Another mode available is `Swipe mode`.

You can change the direction of the swipe by toggling between `Swipe Y` and `Swipe X` in the app menu controls.

![swipe](https://geoservices.leventhalmap.org/docs/media/gif/swipe.gif)



### opacity 

The final available overlay mode is `Opacity mode`.

`Opacity mode` can be activated at any time by selecting `Opacity` in the menu layer controls.

In addition to using the range slider to gradually increase or decrease opacity, try selecting "0" or "100" on either end of the slider to quickly toggle the overlay off and on.

![opacity](https://geoservices.leventhalmap.org/docs/media/gif/opacity.gif)



## Compare change {docsify-ignore}


Try setting both the base and overlay layers to historic atlases. What comparisons can you make that show how the city has changed?

Let's compare a few blocks in South Boston between 1885 and 1891...

In `Glass mode`

![compare glass](https://geoservices.leventhalmap.org/docs/media/gif/compare-glass.gif)

In `Swipe mode`

![compare swipe](https://geoservices.leventhalmap.org/docs/media/gif/compare-swipe.gif)

In `Opacity mode`

![compare opacity](https://geoservices.leventhalmap.org/docs/media/gif/compare-opacity.gif)




## Sharing

To share a link to the whole app, or a specific view/location, following these steps:

1. Click the Share button in the upper-right hand corner <br>
![share](https://geoservices.leventhalmap.org/docs/media/img/share.png)

2. Select the appropriate share option: 
- Share the app
- Share this specific view
- Embed in a website

## Digital collections

While using mosaiced atlas layers inside the Atlascope app is an intuitive way to access the materials, we understand there will certainly be cases where you wish to access high-resolution scans of individual atlas pages, and thus will need to be able to locate these unique items in our [digital collections](https://collections.leventhalmap.org/ "Digital collections").

Or maybe, you even wish to visit the Map Center, and [research](https://www.leventhalmap.org/research/ "Research @ LMEC") with particular atlas pages in person!

For these reasons, Atlascope works symbiotically with our traditional library interfaces, specifically our digital collections and collection-level research guides for the historical urban atlas collection.

In this guide you will learn how to use Atlascope to quickly find atlas plates in the digital collections, download high-resolution images of the maps, or build a citation for any given plate. 

### Use Atlascope to find a plate in the digital collections {docsify-ignore}

1. Use the map or address search to find a location in Atlascope. 
2. Zoom in to the area of interest. 
3. Check the layer menu to ensure you have the correct year and publisher selected.
4. From the app layer controls, select "About this map"
5. Observe the bibliographic information for this volume, and options for finding this resource in the library collections.

![collections options](https://geoservices.leventhalmap.org/docs/media/img/dc.png)

#### View plate boundaries and atlas extent {docsify-ignore}

This option will take you to a page displaying only the layer for the one atlas volume you have selected, and a blue/green outline showing which coverage each page represents. 

![extent](https://geoservices.leventhalmap.org/docs/media/img/extent.png)

When you click on a page boundary, a popup will appear with bibliographic information about that atlas plate, including the digital collections identifier #, and a link to the item in the digital collections.

![popup](https://geoservices.leventhalmap.org/docs/media/img/popup.png)


#### View list of plates in the Digital Collections {docsify-ignore}

This option will bring you to a query in the digital collections returning all results associated with that atlas's call number. This will essentially be a gallery of thumbnails. You will still need to page through the results to find the plate with the location of interest.

> *Hint:* Viewing the list of plates in the digital collections is a great way to locate the index page for any given atlas. You may want to use the index page to find that atlas's symbology key. Each publisher uses different colors and markings, so the legend on the index page can be helpful.


#### Find this plate in the Digital Collections {docsify-ignore}
This option will bring you to a page with only that atlas layer again, but this time, it will be zoomed in on the area you had been engaging with in Atlascope. 

This is generally the best way to find a specific plate in the digital collections, as this tool will remember where you were looking in Atlascope, and bring you right to that item in the digital collections. 

1. After clicking "Find this plate in Digital Collections," click on the exact area you are looking for, and a popup should appear with bibliographic information.

2. At the bottom of the popup, click "View this plate in digital collections"


3. To download a high-resolution scan, navigate to `Downloads` and select `Master (full resolution, uncompressed)`

4. To cite this plate, select "Cite". A citation will be automatically generated.




## All atlases @ BPL

### Atlases not included in Atlascope {docsify-ignore}

While Atlascope includes an amazing number of atlases from the BPL collections covering Boston and surrounding towns, it does not include a significant portion of atlases available for research at the BPL.
> **Atlases not in Atlascope** <br>
> - Atlases outside of Boston Proper for most towns in Massachusetts - *If you would like to support expanding the geography, please contact us.*
>
> - Atlases published after 1923 where rights are still retained by the copyright owner. This includes most of the twentieth-century Sanborns.

### Coming in to research {docsify-ignore}

Though you cannot access these important archives in Atlascope or the digital collections quite yet, you **_can_** research with them in person. Here's how:

1). Submit a reference request using our [research form.](https://www.leventhalmap.org/research/ "Research @ LMEC")

2). Use our libguides to find a complete record of what's available.


### Using the libguides {docsify-ignore}

> Libguides → http://guides.bpl.org/urban-atlases
>
> The **BPL Urban Atlases Libguides** provide a comprehensive citation of every urban atlas available within the state of Massachusetts at the BPL.
> 
> Here we will describe how to use the libguides to determine the best way to access any given atlas, depending on the following factors:<br>
> **→** Whether or not it has been digitized and added to the Digital Collections and <br>
> **→** Whether or not it has already been added to Atlascope <br>
> **→**  Whether it is still under copyright and must be accessed in person.



Navigate to the [Historical Urban Atlases of Boston Libguide.](https://guides.bpl.org/urban-atlases "Urban Atlas Libguide")


To find a list of citations for all urban atlases available at the Boston Public Library, organized by neighborhood and chronology, select `List of Urban Atlases`.

In addition to this comprehensive citation list of every atlas available at the Boston Public Library, the Boston area libguide has a tab `Find by Map` which visually displays records for all Boston atlases and places them on a map interface, grouped by neighborhood. Many of these atlases have been digitized and added to Atlascope already, while others are still pending processing, or cannot be digitized yet because they are under copyright. 

Choosing an atlas from the neighborhood map menu dropdown will let you know the best way to access that item.

If you add a menu item for something that has been added to Atlascope, a link will appear that will bring you to that item in Atlascope. If you select a menu item that has not yet been added to Atlascope, a boundary extent layer will appear on the map, giving you useful bibliographic popup information about each atlas plate as a placeholder until we are able to extend direct access to the mosaiced imagery. 


If you are looking for towns outside of Boston, from the guides.bpl.org/urban-atlases page, navigate to **Related Resources** tab on the left, select `Historical Urban Atlases of Massachusetts Towns @ the BPL`.


This will bring you to a complete listing of historical town atlases available for research at the BPL. They are organized by County.

For questions related to researching with the BPL holdings, please do not hesitate to get in touch via our [research form](https://www.leventhalmap.org/research/ "Research @ LMEC") or via email at reference@leventhalmap.org. 



## All layers in Atlascope {docsify-ignore}

Atlascope also provides a way to see all layers included in the app. 
Try zooming far out on the map to see all of the layers available. 
Select one from the dropdown menu to be brough to that atlas layer. 


## Mosaic links

We think one of the coolest aspects of creating high-resolution layers of each atlas is our ability to share them with you.

This section of the guide will give instructions on how to bring in the mosaic of any atlas in Atlascope to your own GIS project. 


The tiles for each volume are accessible by selecting `About this map` and then copying the link under `XYZ Tile Endpoint`

![tiles](https://geoservices.leventhalmap.org/docs/media/img/tiles.png)

This link can be brought into any geospatial software -- desktop software like ArcMap, ArcGIS Pro, and QGIS, cloud mapping platforms like ArcGIS Online, Carto and Google Maps, and you can even use them to build your own Javascript web apps, like we did with Atlascope!

For any questions centered on using these tiles as layers in your own project, or any questions related to geospatial data and mapping, please do not hesitate to reach out to us via our [geospatial research form.](https://leventhalmap.org/research/geospatial-data "Geospatial Research @ LMEC")

