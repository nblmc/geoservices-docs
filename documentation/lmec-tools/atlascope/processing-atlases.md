# Introduction {docsify-ignore}

The LMEC collection of fire insurance and real estate atlases of metropolitan Boston is in the process of being imaged, georeferenced, and mosaiced to produce continuous-coverage, geographically-locatable versions of these historic objects.

This documentation contains information on how to create the underlying data sources of the Atlascope project, including raster imagery, vector boundary files, and metadata records. It assumes prior knowledge with GIS and data tools.

For a more contextual and step-by-step overview of the process, visit our [create mosaics guide](#/guides/tools-guides/atlascope/create-mosaics "create mosaics guide").



# Requirements

- Scans of the individual atlas plates (recommended ≥ 300 dpi TIFF format)
- GIS Application - this documentation is written for QGIS
- Text editor - Atom, Notepad ++, Visual Studio Code or other
- FTP Client - these guides are written for Cyber Duck
- (**$**) Cloud storage - BPL uses low-cost Boston-based Wasabi
- (**$**) External hard drive for backup (optional/recommended) - tiles are large



# QGIS workspace

To set up the QGIS workspace for this process, qgis plugins → python console → show editor
copy the below script into the editor & press **run**

```shell
for layer in [layer for layer in QgsProject.instance().mapLayers().values()]:
  if layer.name().lower() in ["openstreetmap", "index", "boundary"]:
    continue
    layer.renderer().setOpacity(0.6) #can change 6 for different opacity value
    provider = layer.dataProvider()
    provider.setNoDataValue(1,0) 
    layer.triggerRepaint()
```
# File structure

This project creates many different files, some of which are temporary, intermediary working files, others which will be backed up long-term. 

> The files which will be backed up long term are:<br><br>
**Spatial imagery:** spatially-aligned versions of the archival tiffs for each atlas plate (.geotif)<br>
**Gcps:** control points created for spatial alignment purposes (.txt)<br>
**Boundary:** vector polygon where each feature corresponds to an atlas plate. Used for masking out unwanted data for the mosaic & to link tiles back to unique digital collections items by joining with library metadata (.geojson)<br>
**Mosaic:** massive, spatially aligned imagery file of all masked plates stitched together (.geotif)<br>
**Tiles:** tiles are generated from the large mosaic.tif file (TMS .png tiles, zoom levels 13-20)<br>


![file structure](https://geoservices.leventhalmap.org/docs/media/img/data-structure.png)

# File backup 

The various scripts and processes in this project generate many temporary working files that are worked with and stored locally. There is a backup strategy in place for data that should be archvied long-term:

![file structure](https://geoservices.leventhalmap.org/docs/media/img/data-backup.png)



# Source imagery
To create archival copies of all individual plates associated with any BPL barcode, place a copy of [get-all-by-barcode.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/get-all-by-barcode.py "Download all tiffs script") inside the atlas barcode folder & run from the terminal. You will need to change the part of the script that specifies which particular barcode to download. Running this will take approximately twenty minutes, and will result in a folder entitled "arch_tiff" containing all plates associated with that barcode. 


# Georeferencing

**Georeferencing tool:** <br>
QGIS plugin GDAL Georeferencer is used for georeferencing. Using this tool, .geotifs and .txt gcps are exported for each individual atlas plate. 

**Bit depth:** <br>
Images should have been scanned at 8-bit depth. If they are 16-bit, you will need to convert the images to 8-bit.

**Projection:** <br>
Individual plates are referenced to EPSG: 4326 projection and transformed during the mosaicing process to 3857 to be compatible with web mapping. Please note that subsequent steps in this process are projection-dependent, and if an alternate projection is chosen during georeferencing, the mosaicing and tiling process will fail. Step-by-step instructions for setting up a proper georeferencing environment for this project are available in [create mosaics → georeferencing](#/guides/tools-guides/atlascope/create-mosaics?id=georeferencing "create mosaics guide").


**Transformation settings:**<br>
Transformation type: Polynomial 1 <br>
Resampling method: Cubic <br>
Target SRS: EPSG: 4326 - WGS 84 <br>
Output Raster: spatial_imagery/**identifer** <br>
Compression: LZW <br>
Save GCP points: checked <br>
Load in QGIS when done: checked <br>
Everything else unchecked <br>


**Importing gcps:** <br>
It is possible to use GDAL Georeferencer to import previously created gcps, rather than create them from scratch. Step-by-step instructions for doing so are available in [create mosaics → importing gcps](#/guides/tools-guides/atlascope/create-mosaics?id=special-instructions "create mosaics guide").

# Handling insets
For plates containing insets, the procedure is to georeference the plate twice, once for the main section of the plate, once for the inset (a portion of the map will be wrong in both cases). Irrelevant data is masked out later from each plate during the mosaicing process. 

Some plates may contain more than one inset. Files are named with suffixes identifier_inset1, identifier_inset2, and so on, depending on how many insets each plate contains. 

When generating the masking footprint, you will want to be sure to create a unique polygon feature for each inset to ensure all map areas depicted in insets are included in the final mosaic. 

When joining the masking footprint with the bibliographic metadata, the inset should have its own record in the metadata csv. All of the fields for this record should have identical values to that of the "main" plate. The only field for the inset record that should have a different value than the main plate is the identifier value (identifier vs. identifier_inset1).


# Masking

Footprint layers are used to:

1. Mask out superfluous or empty “white space” on historical atlas plates, a necessary step for seamless mosaicing
2. Store references to plate-level library metadata, ultimately included in front-facing interfaces for the purpose of increasing accessibility to the historical archives

Broadly, this is accomplished by:

1. Generating a polygon layer that includes a feature for every georeferenced plate in the atlas, and editing the geometry of these features to appropriately reflect the desired extent of the plate data (including insets)
2. Joining the newly created footprint with plate-level library metadata

To ensure a feature exists for every spatial image in the volume, you can use [create-plate-index.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/create-plate-index.py "script to autogenerate footprint layer"). This script will automatically generate a feature for every .tif file in whatever folder it is run from. It will also create a field in the newly generated vector file containing the correct identifier number as a value for every feature/record. 






- To change image transparency, right-click the layer in the table of contents → Properties → Legend → use arrow to add opacity slider to Used Widgets. After clicking OK, slider will appear in layer list

- Properties → Transparency → **No Data** set to **0** removes the black border

- Make sure snapping is set to **Vertex and Segment**, and **Topological Editing and Snapping on Intersection** are **enabled**
Project → Snapping options

![Snapping](https://geoservices.leventhalmap.org/docs/media/img/snapping.png)

- The option enable topological editing is for editing and maintaining common boundaries in features mosaics. QGIS ‘detects’ shared boundary by the features, so you only have to move a common vertex/segment once, and QGIS will take care of updating the neighboring features.

- Setting the snapping radius to a lower value will allow for more control over where to place points (15 px seems to work well)

- There should not be gaps or overlap between map plate boundaries

**EDITING TOOLS OVERVIEW**

- Vertex tool  (click, move mouse to new location, click) moves an already existent “node” <br>
![Vertex tool](https://geoservices.leventhalmap.org/docs/media/img/vertex.png)

- Double-clicking on a line will allow the creation of a new vertex

- Holding down the space bar will temporarily allow you to pan around

- This info button will tell you which plate the boundary refers to (make sure index layer is highlighted in layer list) <br>
![Start georeferencing](https://geoservices.leventhalmap.org/docs/media/img/info.png)

- Select a vertex & press the delete key to delete

- Selecting a data layer in the layer list and pressing the space bar will toggle the layer on & off



## Steps

### Plate geometry {docsify-ignore}


1. Change the Airtable field “footprint” from “to do” to “in progress”

2. Make a copy of [create-plate-index.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/create-plate-index.py "script to autogenerate footprint layer") inside the folder containing the georeferenced images (spatial_imagery)

3. Open a terminal at the folder containing imagery by **right-clicking → New terminal at folder**

4. Run the following command:

```shell
$ python3 create-plate-index.py
```

5. Open QGIS

6. Add newly generated `atlas_root/spatial_imagery/index/index.geojson` to map

> This is an index file that contains features with the extent of each georeferenced image. Each polygon corresponds to a record in the index attribute table, with the plate id name (e.g. 0001) as the value for field “identifier”. You will need to edit the boundaries/vertices of each polygon to create a masking footprint suitable for mosaicing.<br><br>
Once each feature has been edited appropriately, this layer will be exported and used both to mask the imagery in preparation for mosaicing *and* as important front-end data in the discovery application.


7. Add the imagery of a feature that needs editing, along with imagery of adjacent plates, for comparison

8. Drag the index json to the top of the layer list, so that it sits on top of the imagery, and adjust the transparency so the imagery is visible

9. Open the attribute table

10. Click on the pencil icon to toggle editing

11. Remove the .tif suffix from the identifier values, so that values are only the plate name

> **G1234_B6G475_S2_1867v1_0006.tif**  → becomes → **G1234_B6G475_S2_1867v1_0006**

12. Click the pencil & save the edits

13. Exit the attribute table

### Drawing & editing {docsify-ignore}

1. Main document menu → toggle editing

2. Make sure snapping is set to **Vertex and Segment**, and **Topological Editing and Snapping on Intersection** are **enabled**
Project → Snapping options

![Snapping](https://geoservices.leventhalmap.org/docs/media/img/snapping.png)


- The option enable topological editing is for editing and maintaining common boundaries in features mosaics. QGIS ‘detects’ shared boundary by the features, so you only have to move a common vertex/segment once, and QGIS will take care of updating the neighboring features.

- Setting the snapping radius to a lower value will allow for more control over where to place points (15 px seems to work well)

- There should not be gaps or overlap between map plate boundaries



> Where to draw the new footprints on each plate is up to your discretion; general guidelines require the edges of map plates to match up to one another and as much information useful to a user is preserved. <br><br>
If there are areas of overlap, select the portion from whichever map has the most useful/detailed information (street names and historic street numbers are visible, etc). <br><br>
There will inevitably be areas where the maps do not match exactly or some information/features will be sacrificed but the goal is to limit this and make the most useful and aesthetically pleasing map mosaic possible.
Treat every property like it is the one a researcher wants to find!

!> FINAL STEP: When you have finished your footprint, run a validity check on the geometry to ensure all features are valid. You can do this by selecting **Vector → Geometry Tools → Check Validity**

Make sure the correct file is selected; all other options can be left at default.

If all features are included in the Valid Output file, proceed. If any features are included in the Invalid Output file, correct the geometry before proceeding. (Refer to correct snapping settings to ensure you are creating polygons with no overlapping geometry)

**Example of successful validity check:**
![check-validity](https://geoservices.leventhalmap.org/docs/media/gif/check-validity.gif)

### Joining metadata {docsify-ignore}


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

4. To find metadata for the atlas you are working on, navigate to the shared Maps drive/metadata. There is a file titled "metadata_clir.csv". Make a local copy wherever your temporary working files are.

5. Open the copy of metadata_clir.csv. CTRL + F and search for either an identifier you know is in your atlas, or the atlas call number. Highlight the records for every plate in the atlas, and copy the values into your new, atlase-specific excel workbook.

6. In the new, atlas-specific excel workbook, you can delete the row "call_no," and any records not pertinent to the plates you need metadata for (example: index plate, title page)


6. Save the file, ensuring it is saved as a CSV.

7. Add metadata.csv to QGIS **Layer → Add Layer → Add Delimited Text Layer**

> File format = **CSV** <br>
> Number of header lines to discard = **0** <br>
> “First record has field names” = **CHECKED** <br>
> “Detect field types” = **UNCHECKED** <br>
> Geometry definition = **No Geometry (attribute only table)**

!> If no data found in file: <br> 1. Open metadata in Atom <br> 2. [line-ending-selector](https://atom.io/packages/line-ending-selector "line-ending-selector") <br> 3. Save <br> 4. Try again!


8. Add → Close

9. Join Boundary polygon data & metadata.csv <br>
**Right click boundary layer → Properties → Joins → Green Plus Sign (bottom left)**

> - Join Layer = **metadata**
> - Join field = **identifier**
> - Target field = **identifier**

10. Open the Boundary attribute table to make sure everything joined properly, and all of the values have populated


### Exporting footprint {docsify-ignore}

1. **Right click layer containing join → Export**

2. **Save Features As**

> - Format = **GeoJSON**
> - Destination path = `atlas_root/footprint/Masking.geojson`
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
![Boundary.shp fields](https://geoservices.leventhalmap.org/docs/media/img/fields.png)

9. **Right-click Boundary file → Export → Save Features As**

> - Format = **GeoJSON**
> - Destination path = `atlas_root/footprint/Boundary.geoJSON`
> - CRS: **EPSG 4326 - WGS 84**

10. Update the Airtable to reflect that the footprint has been completed, ensure that the footprint data is accessible on the Maps Drive for mosaicing, and if imagery is also completed, post "atlas short description ready to mosaic" to #atlascope-general slack channel.


## Special Instructions

### Inset metadata {docsify-ignore}

If your atlas contains insets:

1. In metadata.csv, copy the record that exists for the whole plate (e.g. if the inset is for `_0004_inset1`, copy record `_0004`)

2. Insert a new row in the spreadsheet with the copied values

3. In the identifier field for the new record you just created, add appropriate inset suffix

4. Every feature you have created or edited in the boundary file **needs to have a corresponding record in metadata.csv** for the one-to-one join to perform correctly

5. The only field where values should differ between insets and corresponding “main” plate (0004 vs. 0004_inset1) is the identifier field. All of the rest of the metadata should be the same.


### Missing plate properties {docsify-ignore}

There may be some cases where the plate field is not included in the library metadata. This field **does** need to be included in Boundary.geojson. Follow these steps:

1. Create a copy of [get-plate-value.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/get-plate-value.py "get-plate-value.py") and place it inside the folder containing Boundary.geojson `atlas/footprint/Boundary.geojson`

2. Open a terminal at the folder containing imagery by **right-clicking → New terminal at folder**

3. Run the following command:

```shell
$ python3 get-plate-value.py
```
4. Follow the prompts, inspecting the plate values in the digital collections

5. Open Boundary.geojson in a text editor and ensure that the plate field was created, and values were populated correctly

# Mosaicing

## Context {docsify-ignore}

In order for individual atlas plates to be combined into a seamless mosaic, they must first be masked, using the footprint boundary layer, to show only relevant map data.

This step involves running a tool that will iterate through each georeferenced atlas plate and mask it to the geometry of the polygon feature in the Boundary footprint layer with the same identifier name. The masked rasters, after being compressed and going through various imagery setting adjustments, will then be mosaiced. The output of running this tool is a large tif file containing the mosaic for the atlas.

If all of the data has been prepared correctly, this tool should work without issues.
If errors are returned, the mosaic will not generate, and you will need to use the error messages to debug issues with the input geoTIFF and footprint data.

## Tips {docsify-ignore}

> You will need to be able to run standalone Python scripts and utilize osgeo tools from the terminal in order to work through this step. Please find documentation on how to [configure a mac](https://geoservices.leventhalmap.org/docs/#/computing/mac-setup "Mac Setup") to these settings. If you wish to configure your Windows environment for this workflow, please do not hesitate to get in touch at reference@leventhalmap.org

## Steps {docsify-ignore}

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


# Tiling


## Creating {docsify-ignore}

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

## Command

9. Run the following command:

```shell
$ gdal2tiles.py -r cubic -p mercator -e -z 13-20 --processes=6 mosaic.tif tiles/
```

> Note: If tiles are being generated too slowly using this process, you can use [gdal2tiles_parallel.py](https://github.com/GitHubRGI/geopackage-python/wiki/Usage-Instructions-for-gdal2tiles_parallel.py "gdal2tiles_parallel").

10. When the tiles have completed, expand the **tiles** directory folder on the hard drive and take note of the auto-generated .html pages. Previewing these pages is a helpful way to ensure the tiles were generated correctly. Open **leaflet.html** in a browser, and ensure the imagery was cached correctly.

> Note: The default opacity value in the auto-generated leaflet.html page is not full opacity, which can hinder the ability to check image quality of the tiles. To increase opacity of the tiles for proper preview, open leaflet.html in a text editor and change `opacity: 0.7` to `opacity: 1` in the line below. <br>
![Opacity default](https://geoservices.leventhalmap.org/docs/media/img/opacity-default.png)



10. At the beginning of the tile generation process, mosaic.tif was copied directly into the `Documents/atlas-temp-tiles/barcode` folder, in order to generate tiles at the correct local directory level. Drag mosaic.tif into `CLIRSTORAGE/barcode/src/mosaic` to permanently store the mosaic TIFF in the src folder.

# Sharing

Open the tiles folder in a new terminal.

Delete blank tiles by running this command:

```shell
$ find . -type f -size -335c -delete
```
Once that has completed, upload tiles to Wasabi by running this command:

```shell
$ for i in {13..20}; do cd $i; for f in *; do s3cmd put --recursive $f s3://urbanatlases/BARCODE/tiles/$i/; done; cd ../; done
```

If s3cmd is not installed, you can do so by running `brew install s3cmd` and configuring our Wasabi credentials by following the steps [here](https://wasabi-support.zendesk.com/hc/en-us/articles/115001757791-How-do-I-use-s3cmd-with-Wasabi- "here")


From the Airtable, open the atlas "mosaic_URL" link. Check that high-quality tiles are appearing for the entire coverage extent of the atlas, at all desired zoom levels.

When tiles have successfully uploaded to the cloud storage, download a copy of the "tiles" folder inside `CLIRSTORAGE/barcode` to back them up on the external hard drive, and delete the local copy created.

To publish the atlas in Atlascope and populate the urban atlases libguide with updated information, follow the steps in `Maps Center Drive → Geospatial → handy-reference → internal-guides → publishing-atlases`

# Backing up

When you have finished processing an atlas the backup file structure should look as follows:

**Maps Center Drive:**

`Maps Center → GEOSPATIAL →  urban-atlases →  barcode`

![M drive backup footprint](https://geoservices.leventhalmap.org/docs/media/img/mdrivebackup.png)

![M drive backup gcps](https://geoservices.leventhalmap.org/docs/media/img/mdrivegcps.png)

The Maps Center drive should be backed up only with the vector data that has resulted from this project. Any other files, especially imagery, should be cleaned out, after ensuring all of the imagery files are backed up in their proper locations.

Footprints should be saved as geoJSONs.


**External Harddrive:**

All atlas data should be backed up here with the following structure:

![clirstorage](https://geoservices.leventhalmap.org/docs/media/img/clirstorage.png)

**Wasabi Cloud Storage:**

![wasabi](https://geoservices.leventhalmap.org/docs/media/img/wasabi.png)
