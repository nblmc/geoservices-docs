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


#### Atlas insets

1. Georeference the plate twice. Once for the main section, and once for the inset (a portion of the map will be wrong in both cases)

2. Naming standard: the geoTIFF with the main part of the map should be named normally (identifier with no suffix). The insets will have suffixes that are numbers counting up (depending on how many insets there are, beginning at 1 (identifier_inset1, identifier_inset2, and so on.)

3. In subsequent steps, the geoTIFFS for each plate will be imported and treated as completely separate plates that each need their own polygon feature in the masking footprint layer (the irrelevant/overlapping portions will be masked out by the footprint during the mosaicing process)

4. When adding metadata, the inset should have its own record in metadata.csv. All of the fields for this record should have identical values to that of the "main" plate. The only field for the inset records that should have a different value than the main plate is the identifier value (identifier vs. identifier_inset1).


#### Multiple-scale volumes

Historical urban atlases for densely populated cities are likely to include plates that are homogenous in scale.

On the other hand, it is common in atlases representing less densely-populated areas, like in county and town atlases, to find plates at various scales. When this occurs, separate mosaics should be created for each scale.

1. Within the working atlas root directory, create two sub-folders that will house the mosaic data for each scale mosaic. Use the barcode as the folder basename with alphabetic suffixes to differentiate between the scales:
  - example:  39999059011153a, 39999059011153b, and so forth for each scale that exists

2. Create a new record in the Airtable for each scale mosaic with the appropriate barcode ID

3. Proceed with the georeferencing process as normal. A separate footprint will also need to be created for each scale.






## Imagery check

## Create footprint

## Footprint check

## Create Mosaic

## Generate tiles

1. When the mosaic has finished, set up a directory on the CLIRSTORAGE external hard drive for the atlas.
Copy the atlas **barcode** from the Airtable, and create a folder at the root level of the hard drive with folder name **barcode**
*Tiles can be generated from a TIFF file in any location. They are space-intensive, so LMEC generates them on a separate external hard drive. We use the atlas barcode as a volume-level unique id. Organizing files consistently allows for data to be easily iterated through in subsequent geoprocessing and indexing steps for display in the web.*

2. Copy mosaic.tif from the working directory and paste into the atlas barcode folder.

3. Open a terminal at the barcode folder by right-clicking the folder → New Terminal at folder

4. Run the following command:

```shell
$ gdal2tiles.py -r cubic -p mercator -e -z 13-20 --processes=6 mosaic.tif tiles/
```

> Note: If tiles are being generated too slowly using this process, you can use [gdal2tiles_parallel.py](https://github.com/GitHubRGI/geopackage-python/wiki/Usage-Instructions-for-gdal2tiles_parallel.py "gdal2tiles_parallel").

5. When the tiles have completed, expand the **tiles** directory folder on the hard drive and take note of the auto-generated .html pages. Previewing these pages is a helpful way to ensure the tiles were generated correctly. Open **leaflet.html** in a browser, and ensure the imagery was cached correctly.

> Note: The default opacity value in the auto-generated leaflet.html page is not full opacity, which can hinder the ability to check image quality of the tiles. To increase opacity of the tiles for proper preview, open leaflet.html in a text editor and change `opacity: 0.7` to `opacity: 1` in the line below. <br>
![Opacity default](/media/img/opacity-default.png)

6. When you are satisfied with the quality of the tiles, and wish to publish them, create a new folder within the barcode folder titled **"src"**

7. Inside "src" create the following three sub-folders to store backups of important atlas data.
  - "footprint"
  - "gcps"
  - "mosaic"

8. From the working directory, copy any useful **.txt gcp** files into `CLIRSTORAGE/barcode/src/gcps` and **Boundary.geoJSON** into `CLIRSTORAGE/barcode/src/footprint` folder.

9. At the beginning of the tile generation process, mosaic.tif was copied directly into the barcode folder, in order to generate tiles at the correct directory level. Drag mosaic.tif into `CLIRSTORAGE/barcode/src/mosaic` to permanently store the mosaic TIFF in the src folder


## Publish tiles

1. If not already installed, download and install [CyberDuck](https://cyberduck.io/ "CyberDuck")

2. Click "Open Connection"

3. Select Amazon S3 in the dropdown menu

4. Connect with your cloud storage credentials. *LMEC credentials are stored in `Maps Center → GIS → CLIR → quick-reference → wasabi-credentials`*

5. You will see the file directory appear. Create a new folder with the atlas barcode, and upload the tiles and src folders from the hard drive for that atlas into this new folder.

> Note: As the uploads are generally large, it works best to upload one set of tiles at a time.

A transfer status dialog box will appear with feedback on the anticipated transfer time. When the tiles and source files have completed uploading, perform the following tasks to ensure tiles are discoverable: *These steps are specific to LMECs particular front-facing discovery environments.*

6. From the Airtable, open the atlas "mosaic_URL" link. Check that high-quality tiles are appearing for the entire coverage extent of the atlas, at all desired zoom levels.

7. Change the "status" field in the Airtable to **"Complete"**

8. in #CLIR-general, post "x atlas is ready for libguide citation updates and ingest into app"
