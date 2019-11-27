<head>
<title>Mosaicing Atlases</title>
</head>


# Mosaicing and Publishing Atlas Plates

This guide will walk through a process that begins with a [collection of individual atlas plates](https://collections.leventhalmap.org/search?utf8=%E2%9C%93&q=39999059015550 "Cambridge 1873 plate list"), and results in a [mosaiced tiled map service](https://geoservices.leventhalmap.org/atlas-extent-viewer/index.html#39999059015550 "Cambridge 1873 mosaic").


The broad contours of this workflow include georeferencing individual atlas plates, masking them using a footprinting layer to only reveal appropriate data, stitching plates together to create a raster mosaic, and publishing the stitched mosaic as a tiled map service.


Some instructions pertain to particulars of the Leventhal Map & Education Center (LMEC) at the Boston Public Library (BPL) collections, for example, file naming structures, metadata standards, and so on, but the idea behind and implementation for each step can be applied universally. *BPL-specific instructions will be flagged, to indicate one should consider their own institution or project-specific details.*

The software and tools described in this process are all free. Cost lies in staff time required to process the imagery, and in data storage for resulting tile services.


The guides for each step in the process have been written to include context, tips for efficiency (e.g. when adding a control point in QGIS, hold the spacebar to pan the map), step-by-step instructions for working through the process, and any special notes or considerations.

A workflow for mosaicing historical atlases could take many different forms. Please find below the one we have discovered - through trial and error - works best for creating low-cost, high-quality tiled map services of historical atlas mosaics in open formats. This workflow relies on the use of QGIS and free-standing Python scripts in a Mac environment. Please do not hesitate to get in touch for further inquiry, or for help navigating special considerations centered on the use of Windows or the ESRI suite: *reference@leventhalmap.org*


## Requirements/Recommendations
- Scans of the individual atlas plates (recommended ≥ 300 dpi TIFF format)
- GIS Application - these guides are written for QGIS
- Text editor - Atom, Sublime, Notepad ++, or other
- FTP Client - these guides are written for Cyber Duck
- (**$**) Cloud storage - BPL uses low-cost Boston-based Wasabi
- (**$**) External hard drive for backup (optional/recommended) - tiles are large





## Georeferencing

### Context

Individual atlas plates must be spatially aligned before becoming the input data for a raster mosaic.

Georeferencing refers to the process of adding pairs of corresponding location points to both a digital map and a non-spatial image file. After enough ground control points (gcps) have been defined, image files can be exported with various other image settings (compression type, file format, and so on) to create images that have desired image properties and are “spatially aware.”

The following workflow will produce two separate formats of data that are important to preserve:

- **Spatial imagery** - TIFF files that have been georeferenced and exported as geoTIFFs and
- **Ground control points (gcps)** - .txt file containing gcp coordinates

While the spatial imagery will exist as TIFF files that can be fed as input into the mosaicing process, the ground control points (gcps) are important from a long-term preservation standpoint. For each atlas plate georeferenced, a .txt file with a list of x,y coordinates for each control point should also be exported. This .txt file is an excellent way to make the most out of the time spent georeferencing for the following reasons:
- .txt files are small compared to raster imagery -- great for long-term preservation
- When a geoTIFF has been exported after referencing, the saved image will exist as a capture of all the choices made at the time the image is exported. This means compression settings, file type, resampling methods, spatial alignment and other properties are baked into a new TIFF file. Gcps, on the other hand, can be used as future input to generate spatial imagery with any number of settings. Ensuring that gcps are exported after every plate has been georeferenced ensures that spatial alignment is backed up, even in the case that image files are somehow saved with incorrect settings or properties.
- If a plate is aligned incorrectly, one can simply alter gcps which have been backed up, rather than restart the georeferencing process from scratch.


Another aspect to take into account is whether the historical images at hand allow for the automation of the alignment process. If so, it may be worthwhile looking into workflows that speed up this process.

The 19th century historical urban atlases for which these guides were created contain plates that are too nuanced and lacking in standardization to automate the alignment or masking processes.  Similarly, many plates are laden with map insets. For these reasons, it would be difficult, if not impossible to automate the alignment process and still expect mosaicing results that achieve an equal level of precision as delivered by the included workflow.

One should consider the data at hand -- if the maps requiring alignment have standard, rectangular extents, [workflows](http://www.e-perimetron.org/Vol_14_3/Fleet.pdf "NLS Automated Georeferencing") have been developed for drastically speeding up the georeferencing process. This guide describes the process of manual georeferencing.


### Tips

- To adjust the transparency of a layer, right click on the layer in the QGIS Layers window and navigate to Properties → Transparency. This will allow you to compare the image location against the basemap


- To add an opacity slider to a layer, navigate to the Legend tab in the Properties and move the Opacity Slider to the Used Widgets side



### Steps

1. Update the asset management table by changing **imagery** and **control points** fields from "to do" to "in progress" *LMEC uses an Airtable database to keep track of the status of the ~100 atlases in this project*

2. Open QGIS

3. Add a basemap **Browser →  XYZ Tiles →  Open Street Map**

4.  Set the projection to WGS 84. At all times in the bottom right of the QGIS document, EPSG should read 4326. **Project → Properties → CRS WGS 84 - EPSG: 4326 → Apply** *Individual atlas plates georeferenced in WGS 84 are compatible with the BPL Map Warper overlay viewer embedded in the LMEC digital collections. You may consider using CRS WGS 84 / Pseudo Mercator - EPSG: 3857, if georeferencing only for the purpose of creating raster mosaics. Choosing at different projection at this step will require other tweaks to the workflow.*

![Check projection](/media/img/proj-check.png)

5. Open **Raster → Georeferencer** The Georeferencing plugin comes automatically installed with recent versions of QGIS. If you do not see it, it is because it has not been enabled. To enable: navigate to **Plugins → Manage & Install Plugins → Installed** and make sure the box next to **Georeferencer GDAL** is CHECKED

6. Open the TIFF you wish to georeference in the georeferencer, by clicking the blue checkered add raster icon in the menu banner.<br>
![Add raster](/media/img/add-raster.png)

<details>
<summary>Locating and managing BPL source imagery</summary>

> - Locate the correct atlas using BPL [town](http://guides.bpl.org/mass-urban-atlases "Massachusetts Town Atlases") and [city](http://guides.bpl.org/urban-atlases/list "Boston Urban Atlases") libguides <br>
> - Included under the volume-level citation in the libuide is a link to a list of all of the plates in that volume in the digital collections.<br>
> - In the list results, observe the range of plate numbers or letters in the atlas, the number of plates to be included in the mosaic, and how many of these plates need to be georeferenced (some will be non-cartographic front matter, like the title plate)<br>
> - Open one of the individual maps. Note the **identifier** and **barcode** field in the metadata. <br>
> - The **identifier** is the unique ID for every plate-level digital object. The literal string observed as the value for the **identifier** field in the object's metadata should be the file name every time you are exporting both geoTIFFFS and control points<br>
> - The **barcode** is the unique ID at the volume level

</details>

7. After you have added one of the TIFFs to the **GDAL Georeferencer**, click the Add Point button in the menu banner
![Add point](/media/img/qgis-add-gcp.png)

8. Choose a spot on the historical map for which you think you can find a corresponding modern location. Intersections are a good place to start, if they still exist!

9. Choose to add the corresponding location **From Map Canvas**
![From Map Canvas](/media/img/map-canvas.png)

10. Find the location on the modern map

11. Click OK on the Enter Map Coordinates dialog box. In the **GDAL Georeferencer**, the map will not automatically snap to the correct location. Preview is not available until a few points have been added.

12. Add two more control points, so that there are three total, attempting to spread the gcps on opposite corners of the map.

13. When there are three points, click the green **Start Georeferencing** button <br>
![Start georeferencing](/media/img/start-geo.png)

14. The transformation settings will open. Select the following options:

!> **Transformation type:** Polynomial 1 <br>
**Resampling method:** Cubic <br>
**Target SRS: EPSG:** 4326 - WGS 84 <br>
**Output Raster:** spatial_imagery/**identifer** <br>
**Compression:** LZW <br>
**Save GCP points:** checked <br>
**Load in QGIS when done:** checked <br>
**Everything else unchecked** <br>

15. Click the green **Start Georeferencing** button again. A progress bar will appear.

16. The new file will be added to the QGIS document. Look at it closely to make sure everything is lining up properly.

17. To make adjustments to the georeferencing, add more control points, or delete points that are incorrect, return to the **GDAL Georeferencer** window:

    1. Use the GCP table to view error for gcps. Delete incorrect points by highlighting the row and right-clicking.

    2. When new points are added or changes are made, click the green **Start Georeferencing** arrow again to update the geoTIFF. The updated image will be added to the map document.

    3. Make sure that the file exported has the correct **identifier**.tif naming convention and is saved in a folder in the working atlas directory titled "spatial_imagery"

18. When the final TIFF file has been georeferenced in a satisfactory manner and exported, navigate to the `spatial_imagery` folder. Open the .txt file in a text editor to ensure that the points are saving correctly. <br><br>
![GCPs example](/media/img/gcps-example.png)

19. Drag the .txt gcp file from `spatial_imagery` into a newly created folder in the working directory at the atlas root level titled `gcps`

20. If, for some reason, they did not export correctly, it is possible to export them by navigating back into the **GDAL Georeferencer** window and selecting **File → Save GCP points as ...**

21. Repeat this process with all plates in the atlases

22. Complete and submit an imagery quality control checklist. *LMEC uses peer-editing to ensure data has been created and processed at a high-quality*









### Special instructions

#### Importing gcps

This section of the guide describes how to import an existing gcp .txt file rather than having to manually add points for spatial alignment. This comes in handy when:
- Imagery was accidentally exported with less-than-ideal settings, resulting in poor image quality
- Spatial alignment is slightly off, and needs to be fixed


1. Create a new folder in the working atlas root directory titled **spatial_imagery**. This is where the new spatial imagery will be saved. If there is already a file named "spatial_imagery," delete it

2. Open QGIS and set up the document by adding a basemap **Browser → XYZ Tiles → Open Street Map** and setting the coordinate system **Project → Properties → CRS WGS 84 - EPSG: 4326 → Apply**

3. If a footprint already exists for this atlas, bring the Boundary file into QGIS as a way to ensure that the geoTIFFS align with each other correctly. Use the opacity slider to adjust transparency of the layer.

4. Open **Raster → Georeferencer** and select **Add Raster** to open the original TIFF.

!> Make sure you are opening the archival quality digital scan. Do not open any previously referenced geoTIFFS, as this will defeat the purpose of rereferencing with new settings to increase image quality

5. Instead of manually adding new points, you will load existing gcps. There are three ways to do this:

    1. **File → Load GCP Points**

    2. Menu icon <br>
    ![Import gcps](/media/img/import-gcps.png)

    3. Keyboard shortcut ⌘ L

When the file search window opens, navigate to the correct .txt file

6. Select **Start Georeferencing** <br>
![Start georeferencing](/media/img/start-geo.png)

7. The transformation settings will open. Select the following options:

!> **Transformation type:** Polynomial 1 <br>
**Resampling method:** Cubic <br>
**Target SRS: EPSG:** 4326 - WGS 84 <br>
**Output Raster:** spatial_imagery/**identifer** <br>
**Compression:** LZW <br>
**Save GCP points:** `unchecked` <br>
**Load in QGIS when done:** checked <br>
**Everything else unchecked** <br>

8. Click the green **Start Georeferencing** button again. A progress bar will appear.

9. The new file will be added to the map document. Inspect the alignment closely. Use the footprint geometry and basemap to ensure the imagery corresponds to the correct polygon feature in the footprint file, and that the alignment is correct.

!> If you find that the alignment is inaccurate and needs to be redone, return to the **GDAL Georeferencer** window, modify points and re-georeference the plate.<br> <br>
Keep in mind any existing footprint has been created to conform to the saved gcps, so any changes made to the spatial alignment of atlas plates will also need to be reflected in edits to the polygon geometry in the masking footprint layer.


If you make any edits to gcps:

> 1. Save the modified gcps in the working atlas directory folder `gcps` by typing command + S in the **GDAL Georeferencer** Window<br>
> 2. The fooprint will no longer be usable until updated to reflect the alignment changes. Make a note of the plates you have altered so you can edit the corresponding polygon features in the footprint layer.

10. **File → Reset Georeferencer** and open the next image from the original scan archival TIFF folder


#### Georeferencing insets

1. Georeference the plate twice. Once for the main section, and once for the inset (a portion of the map will be wrong in both cases)

2. Naming standard: the geoTIFF with the main part of the map should be named normally (identifier with no suffix). The insets will have suffixes that are numbers counting up (depending on how many insets there are, beginning at 1 (identifier_inset1, identifier_inset2, and so on.)

3. In subsequent steps, the geoTIFFS for each plate will be imported and treated as completely separate plates that each need their own polygon feature in the masking footprint layer (the irrelevant/overlapping portions will be masked out by the footprint during the mosaicing process)

4. When adding metadata, the inset should have its own record in metadata.csv. All of the fields for this record should have identical values to that of the "main" plate. The only field for the inset records that should have a different value than the main plate is the identifier value (identifier vs. identifier_inset1).


#### Handling multiple-scale volumes

Historical urban atlases for densely populated cities are likely to include plates that are homogenous in scale.

On the other hand, it is common in atlases representing less densely-populated areas, like in county and town atlases, to find plates at various scales. When this occurs, separate mosaics should be created for each scale.

1. Within the working atlas root directory, create two sub-folders that will house the mosaic data for each scale mosaic. Use the barcode as the folder basename with alphabetic suffixes to differentiate between the scales:
  - example:  39999059011153a, 39999059011153b, and so forth for each scale that exists

2. Create a new record in the Airtable for each scale mosaic with the appropriate barcode ID

3. Proceed with the georeferencing process as normal. A separate footprint will also need to be created for each scale.



## Creating the masking footprint

### Context

This step produces a **footprint** for the atlas. This footprint is a polygon layer used to:

1. Mask out superfluous or empty “white space” on historical atlas plates, a necessary step for seamless mosaicing
2. Store references to plate-level library metadata, ultimately included in front-facing interfaces for the purpose of increasing accessibility to the historical archives

Broadly, this is accomplished by:

1. Generating a polygon layer that includes a feature for every georeferenced plate in the atlas, and editing the geometry of these features to appropriately reflect the desired extent of the plate data (including insets)
2. Joining the newly created footprint with plate-level library metadata
3. Exporting the footprint in geoJSON format for use in front-facing discovery environments

### Tips

- Use the [libguide plate index](https://apps.bpl.org/nblmc/indexes/index-pinney-1861-boston.html "libguide plate index example"), or, if no libguide plate index exists, the [historical index plate](https://collections.leventhalmap.org/search/commonwealth:6h446z575 "historical index plate example") to determine which plates are adjacent to one another and warrant a comparison. <br>
*Prior to offering direct access to high-resolution mosaiced imagery, BPL provided vector plate indices to locate atlas plates by location. Conceptually and in format, these index guides resemble the footprint layer described by this step, but because these indices were created for the purpose of locating plates, and not for mosaicing, they lack the necessary degree of accuracy required to create high-quality mosaics.*

- To change image transparency, right-click the layer in the table of contents → Properties → Legend → use arrow to add opacity slider to Used Widgets. After clicking OK, slider will appear in layer list

- Properties → Transparency → **No Data** set to **0** removes the black border

- Make sure snapping is set to **Vertex and Segment**, and **Topological Editing and Snapping on Intersection** are **enabled**
Project → Snapping options

	- The option enable topological editing is for editing and maintaining common boundaries in features mosaics. QGIS ‘detects’ shared boundary by the features, so you only have to move a common vertex/segment once, and QGIS will take care of updating the neighboring features.

	- Setting the snapping radius to a lower value will allow for more control over where to place points (15 px seems to work well)

	- There should not be gaps or overlap between map plate boundaries

**EDITING TOOLS OVERVIEW**

- Vertex tool  (click, move mouse to new location, click) moves an already existent “node” <br>
![Vertex tool](/media/img/vertex.png)

- Double-clicking on a line will allow the creation of a new vertex

- Holding down the space bar will temporarily allow you to pan around

- This info button will tell you which plate the boundary refers to (make sure index layer is highlighted in layer list) <br>
![Start georeferencing](/media/img/info.png)

- Select a vertex & press the delete key to delete

- Selecting a data layer in the layer list and pressing the space bar will toggle the layer on & off



### Steps

#### Generating geometry


1. Change the Airtable field “footprint” from “to do” to “in progress”

2. Make a copy of [create-plate-index.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/create-plate-index.py "script to autogenerate footprint layer") inside the folder containing the georeferenced images (spatial_imagery)

3. Open a terminal at the folder containing imagery by **right-clicking → New terminal at folder**

4. Run the following command:

```shell
$ python3 create-plate-index.py
```

5. Open QGIS

6. Add newly generated `atlas_root/spatial_imagery/index/index.shp` to map

> This is an index file that contains features with the extent of each georeferenced image. Each polygon corresponds to a record in the index attribute table, with the plate id name (e.g. _0001) as the value for field “identifier”. You will need to edit the boundaries/vertices of each polygon to create a masking footprint suitable for mosaicing.

7. Add the imagery of a feature that needs editing, along with imagery of adjacent plates, for comparison

8. Drag the index shapefile to the top of the layer list, so that it sits on top of the imagery, and adjust the transparency so the imagery is visible

9. Open the attribute table

10. Click on the pencil icon to toggle editing

11. Remove the .tif suffix from the identifier values, so that values are only the plate name

> **G1234_B6G475_S2_1867v1_0006.tif**  → becomes → **G1234_B6G475_S2_1867v1_0006**

12. Click the pencil & save the edits

13. Exit the attribute table

#### Drawing and editing polygons

1. Main document menu → toggle editing

2. Make sure snapping is set to **Vertex and Segment**, and **Topological Editing and Snapping on Intersection** are **enabled**
Project → Snapping options

	- The option enable topological editing is for editing and maintaining common boundaries in features mosaics. QGIS ‘detects’ shared boundary by the features, so you only have to move a common vertex/segment once, and QGIS will take care of updating the neighboring features.

	- Setting the snapping radius to a lower value will allow for more control over where to place points (15 px seems to work well)

	- There should not be gaps or overlap between map plate boundaries




> Where to draw the new footprints on each plate is up to your discretion; general guidelines require the edges of map plates to match up to one another and as much information useful to a user is preserved. <br><br>
If there are areas of overlap, select the portion from whichever map has the most useful/detailed information (street names and historic street numbers are visible, etc). <br><br>
There will inevitably be areas where the maps do not match exactly or some information/features will be sacrificed but the goal is to limit this and make the most useful and aesthetically pleasing map mosaic possible.
Treat every property like it is the one a researcher wants to find!


#### Cleaning and adding metadata


<details>
<summary>Note on BPL metadata particulars</summary>

> - The instructions to join features to library metadata are specific to the ways BPL creates, manages & and stores metadata for its maps<br>
> - These instructions can be applied to other metadata configurations -- the key is that there needs to be a field common to the polygon footprint layer and the bibliographic metadata table for each unique atlas plate in order to complete a one-to-one join between the polygon layer and the tabular metadata table <br>
> - BPL uses the **identifier** field for this join. Joining this polygon layer where each feature represents the geographic extent of a collections item to library metadata increases accessibility to the historical collections items within the context of map-based discovery interfaces<br>

</details>

1. Open a blank workbook in Excel

2. Enter the following field headers for each column:
  - identifier
  - call_no
  - commonweal
  - title
  - plate
  - publisher
  - year


2. Save As → metadata.csv in a folder titled “metadata” in the atlas root directory

3. Prompt “Do you want to keep that format?” YES

4. To find metadata for the atlas you are working on, navigate to the CLIR_Progress Airtable. There is a view titled "METADATA". CTRL + F and search for either an identifier you know is in your atlas, or the atlas call number. Highlight the records for every plate in the atlas, and copy the values into your new excel workbook.

5. In excel, you can delete the row "call_no," and any records not pertinent to the plates you need metadata for (example: index plate, title page)


6. Save the file, ensuring it is saved as a CSV.

7. Add metadata.csv to QGIS **Layer → Add Layer → Add Delimited Text Layer**

> File format = **CSV** <br>
> Number of header lines to discard = **0** <br>
> “First record has field names” = **CHECKED** <br>
> “Detect field types” = **UNCHECKED** <br>
> Geometry definition = **No Geometry (attribute only table)**

!> If no data found in file: <br> 1. Open metadata in Atom <br> 2. [line-ending-selector](https://atom.io/packages/line-ending-selector "line-ending-selector") <br> 3. Save <br> 4. Try again!

If **still no data** after taking above steps, export the entire metadata table from Airtable as a .csv, and copy records from the downloaded copy. Sometimes copying records directly from Airtable preserves some character formatting QGIS does not like. 

8. Add → Close

9. Join Boundary polygon data & metadata.csv <br>
**Right click Boundary → Properties → Joins → Green Plus Sign (bottom left)**

> - Join Layer = **metadata**
> - Join field = **identifier**
> - Target field = **identifier**

10. Open the Boundary attribute table to make sure everything joined properly, and all of the values have populated


#### Exporting the footprint

1. **Right click layer containing join → Export**

2. **Save Features As**

> - Format = **ESRI Shapefile**
> - Destination path = `atlas_root/footprint/Boundary.shp`
> - CRS: **EPSG 3857 - WGS 84 / Web Mercator**

3. **OK**. Boundary file should be added to the map

4. Open attribute table to ensure join is preserved

5. Open **layer properties → Source Fields**

6. Edit field names so that they match standards:

> - identifier
> - commonweal
> - title
> - plate
> - publisher
> - year

7. Click **pencil → Do you want to save your changes → YES**

8. Open attribute table to ensure fields are named properly <br>
![Boundary.shp fields](/media/img/fields.png)

9. **Right-click Boundary file → Export → Save Features As**

> - Format = **GeoJSON**
> - Destination path = `atlas_root/footprint/Boundary.geoJSON`
> - CRS: **EPSG 4326 - WGS 84**

10. Complete and submit a footprint quality control checklist. *LMEC uses peer-editing to ensure data has been created and processed at a high-quality*



### Special Instructions

#### Preparing metadata for insets

If your atlas contains insets:

1. In metadata.csv, copy the record that exists for the whole plate (e.g. if the inset is for `_0004_inset1`, copy record `_0004`)

2. Insert a new row in the spreadsheet with the copied values

3. In the identifier field for the new record you just created, add appropriate _inset suffix

4. Every feature you have created or edited in the boundary file **needs to have a corresponding record in metadata.csv** for the one-to-one join to perform correctly

5. The only field where values should differ between insets and corresponding “main” plate (_0004 vs. _0004_inset1) is the identifier field. All of the rest of the metadata should be the same.


#### Grabbing plate properties for JSON

There may be some cases where the plate field is not included in the library metadata. This field **does** need to be included in Boundary.geojson. Follow these steps:

1. Create a copy of get-plate-value.py and place it inside the folder containing Boundary.geojson `atlas/footprint/Boundary.geojson`

2. Open a terminal at the folder containing imagery by **right-clicking → New terminal at folder**

3. Run the following command:

```shell
$ python3 get-plate-value.py
```
4. Follow the prompts, inspecting the plate values in the digital collections

5. Open Boundary.geojson in a text editor and ensure that the plate field was created, and values were populated correctly



## Mosaicing

### Context

In order for individual atlas plates to be combined into a seamless mosaic, they must first be masked, using the footprint boundary layer, to show only relevant map data.

This step involves running a tool that will iterate through each georeferenced atlas plate and mask it to the geometry of the polygon feature in the Boundary footprint layer with the same identifier name. The masked rasters, after being compressed and going through various imagery setting adjustments, will then be mosaiced. The output of running this tool is a large tif file containing the mosaic for the atlas.

If all of the data has been prepared correctly, this tool should work without issues.
If errors are returned, the mosaic will not generate, and you will need to use the error messages to debug issues with the input geoTIFF and footprint data.

### Tips

> You will need to be able to run standalone Python scripts and utilize osgeo tools from the terminal in order to work through this step. Please find documentation on how to [configure a mac](https://geoservices.leventhalmap.org/docs/#/computing/mac-setup "Mac Setup") to these settings. If you wish to configure your Windows environment for this workflow, please do not hesitate to get in touch at reference@leventhalmap.org

### Steps

1. Copy [mosaic.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/mosaic.py "mosaicing script") into the working atlas root directory

2. Open a terminal at the atlas root directory by **right-clicking → New terminal at folder**

3. Run the following command:

```shell
$ python3 mosaic.py
```

4. You will be prompted with Yes or No questions. If it is your first time attempting to generate a mosaic for this atlas, answer as following:

  - Have you already ensured that band properties are consistent? N
  - Do you need to mask the images? Y
  - Would you like the create the mosaic at the end? Y

> Note: The script is designed to be flexible, so that if it fails on one of the steps due to faulty data, one can skip repeating any successful preceding steps (which are time-consuming!) An example might be: the imagery settings and projection have been standardized across all plates correctly, but the mask failed due to an incorrect masking cutline value. Rather than re-standardize the imagery settings and projections (both of which processes take a fair amount of time) prior to another attempt at masking, one can answer the prompts in a way as to skip these steps, and only execute those necessary.

5. When the mosaic has finished, bring the newly created mosaic.tif file into QGIS

6. Bring in the footprint masking layer, placing it on top of mosaic.tif

7. Adjust transparency on the footrpint masking layer and peer through, checking that all plates were masked correctly. There should be no unexplainable whitespace, and imagery should be included for every area that has a masking polygon feature. It is better to catch errors during this check than after the lengthy tile generation process runs.


## Generating tiles



1. When the mosaic has finished, set up a directory on the CLIRSTORAGE external hard drive for the atlas.
Copy the atlas **barcode** from the Airtable, and create a folder at the root level of the hard drive with folder name **barcode**.
This is where we will store backups of the tiles and source data, in addition to in the cloud storage.

2. Create a new folder within the barcode folder titled **"src"**

3. Inside "src" create the following three sub-folders to store backups of important atlas data.
  - "footprint"
  - "gcps"
  - "mosaic"

4. From the working directory, copy any useful **.txt gcp** files into `CLIRSTORAGE/barcode/src/gcps` and **Boundary.geoJSON** into `CLIRSTORAGE/barcode/src/footprint` folder.

5. Locally on your computer, navigate to `Documents/temp-atlas-tiles`. If this folder does not exist, create one.

6. Inside `Documents/temp-atlas-tiles` create a folder titled atlas barcode. This is where we will generate our tiles.

> *Tiles can be generated from a TIFF file in any location. They are space-intensive to store and upload, so LMEC generates them locally to optimize cloud upload speeds, and then stores them permanently on an external hard drive. We use the atlas barcode as a volume-level unique id. Organizing files consistently allows for data to be easily iterated through in subsequent geoprocessing and indexing steps for display in the web.*


7. Copy mosaic.tif from the working directory and paste into `Documents/temp-atlas-tiles/barcode`

8. Open a terminal at the barcode folder by right-clicking the folder → New Terminal at folder

9. Run the following command:

```shell
$ gdal2tiles.py -r cubic -p mercator -e -z 13-20 --processes=6 mosaic.tif tiles/
```

> Note: If tiles are being generated too slowly using this process, you can use [gdal2tiles_parallel.py](https://github.com/GitHubRGI/geopackage-python/wiki/Usage-Instructions-for-gdal2tiles_parallel.py "gdal2tiles_parallel").

10. When the tiles have completed, expand the **tiles** directory folder on the hard drive and take note of the auto-generated .html pages. Previewing these pages is a helpful way to ensure the tiles were generated correctly. Open **leaflet.html** in a browser, and ensure the imagery was cached correctly.

> Note: The default opacity value in the auto-generated leaflet.html page is not full opacity, which can hinder the ability to check image quality of the tiles. To increase opacity of the tiles for proper preview, open leaflet.html in a text editor and change `opacity: 0.7` to `opacity: 1` in the line below. <br>
![Opacity default](/media/img/opacity-default.png)



10. At the beginning of the tile generation process, mosaic.tif was copied directly into the `Documents/atlas-temp-tiles/barcode` folder, in order to generate tiles at the correct local directory level. Drag mosaic.tif into `CLIRSTORAGE/barcode/src/mosaic` to permanently store the mosaic TIFF in the src folder


## Publishing tiles

1. If not already installed, download and install [CyberDuck](https://cyberduck.io/ "CyberDuck")

2. Click "Open Connection"

3. Select Amazon S3 in the dropdown menu

4. Connect with your cloud storage credentials. *LMEC credentials are stored in `Maps Center → GIS → CLIR → quick-reference → wasabi-credentials`*

5. You will see the file directory appear. Create a new folder with the atlas barcode, and upload the tiles and src folders from the hard drive for that atlas into this new folder.

> Note: As the uploads are generally large, it works best to upload one set of tiles at a time.

A transfer status dialog box will appear with feedback on the anticipated transfer time. When the tiles and source files have completed uploading, perform the following tasks to ensure tiles are discoverable: *These steps are specific to LMECs particular front-facing discovery environments.*

6. From the Airtable, open the atlas "mosaic_URL" link. Check that high-quality tiles are appearing for the entire coverage extent of the atlas, at all desired zoom levels.

7. When tiles have successfully uploaded to the cloud storage, download a copy of the "tiles" folder inside `CLIRSTORAGE/barcode` to back them up on the external hard drive, and delete the local copy created.

7. Change the "status" field in the Airtable to **"Complete"**

8. in #CLIR-general, post "x atlas is ready for libguide citation updates and ingest into app"
