# Georeferencing

## Context

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


## Tips

- To adjust the transparency of a layer, right click on the layer in the QGIS Layers window and navigate to Properties → Transparency. This will allow you to compare the image location against the basemap


- To add an opacity slider to a layer, navigate to the Legend tab in the Properties and move the Opacity Slider to the Used Widgets side



## Steps

<details>
<summary>Locating and managing BPL source imagery</summary>

> - Locate the correct atlas using BPL [town](http://guides.bpl.org/mass-urban-atlases "Massachusetts Town Atlases") and [city](http://guides.bpl.org/urban-atlases/list "Boston Urban Atlases") libguides <br>
> - Included under the volume-level citation in the libuide is a link to a list of all of the plates in that volume in the digital collections.<br>
> - In the list results, observe the range of plate numbers or letters in the atlas, the number of plates to be included in the mosaic, and how many of these plates need to be georeferenced (some will be non-cartographic front matter, like the title plate)<br>
> - Open one of the individual maps. Note the **identifier** and **barcode** field in the metadata. <br>
> - The **identifier** is the unique ID for every plate-level digital object. The literal string observed as the value for the **identifier** field in the object's metadata should be the file name every time you are exporting both geoTIFFFS and control points<br>
> - The **barcode** is the unique ID at the volume level

</details>


1. Update the asset management table by changing **imagery** and **control points** fields from "to do" to "in progress" *LMEC uses an Airtable database to keep track of the status of the hundreds of atlases in this project*

2. Create a folder locally on your computer, or, if you wish to be able to access your atlas project from multiple different locations, on a flash drive. If you are using a flash drive, ensure it is formatted as ExFAT. 

  The folder structure should be: `local storage → temp-atlas-processing → barcode`

3. To download all archival quality geoTIFFs associated with any given atlas, create a copy of [get-all-by-barcode.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/get-all-by-barcode.py "Download all tiffs script") inside the atlas barcode folder. 

4. Open up this new copy of get-all-by-barcode.py in a text editor, and follow the commented instructions in the script, ensuring the barcode field is correct and will download images for the atlas you are working on. 

  This will take approximately twenty minutes to run, and will result in a folder entitled "arch_tiff" containing archival copies of all tiffs included in your atlas. 


2. Open one of the archival tiffs in a photo software to ensure scans for that atlas were imaged with 8-bit depth. If it is 16-bit, you will need to convert the images to 8-bit, or this georeferencing/mosaicing will not work.

2. Once you have ensured the bit depth of the original images is 8-bit, open QGIS

3. Add a basemap **Browser →  XYZ Tiles →  Open Street Map**

4.  Set the projection to WGS 84. At all times in the bottom right of the QGIS document, EPSG should read 4326. **Project → Properties → CRS WGS 84 - EPSG: 4326 → Apply** *Individual atlas plates georeferenced in WGS 84 are compatible with the BPL Map Warper overlay viewer embedded in the LMEC digital collections. You may consider using CRS WGS 84 / Pseudo Mercator - EPSG: 3857, if georeferencing only for the purpose of creating raster mosaics. Choosing at different projection at this step will require other tweaks to the workflow.*

![Check projection](/media/img/proj-check.png)

5. Open **Raster → Georeferencer** The Georeferencing plugin comes automatically installed with recent versions of QGIS. If you do not see it, it is because it has not been enabled. To enable: navigate to **Plugins → Manage & Install Plugins → Installed** and make sure the box next to **Georeferencer GDAL** is CHECKED

6. Open the TIFF you wish to georeference in the georeferencer, by clicking the blue checkered add raster icon in the menu banner.<br>
![Add raster](/media/img/add-raster.png)


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

21. Open the new geoTIFF in a photo editing software, preferably Photoshop. You only need to do this for the first plate in every atlas, to ensure bit depth of archival scans is correct. If it opens normally, proceed georeferencing the rest of the plates. If the geotiff will not open, you will need to run script convert-16-to-8-bit-tiffs.sh before proceeding.

22. In the QGIS georeferencer, select **File → Reset Georeferencer**

23. Repeat this process with all plates in the atlases

24. Ensure all spatial imagery and ground control points are backed with the [correct backup structure](https://geoservices.leventhalmap.org/docs/#/atlascope/creating/backup "backup").

25. Complete and submit an imagery quality control checklist. *LMEC uses peer-editing to ensure data has been created and processed at a high-quality*









## Special instructions

### Importing gcps

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


### Georeferencing insets

1. Georeference the plate twice. Once for the main section, and once for the inset (a portion of the map will be wrong in both cases)

2. Naming standard: the geoTIFF with the main part of the map should be named normally (identifier with no suffix). The insets will have suffixes that are numbers counting up (depending on how many insets there are, beginning at 1 (identifier_inset1, identifier_inset2, and so on.)

3. In subsequent steps, the geoTIFFS for each plate will be imported and treated as completely separate plates that each need their own polygon feature in the masking footprint layer (the irrelevant/overlapping portions will be masked out by the footprint during the mosaicing process)

4. When adding metadata, the inset should have its own record in metadata.csv. All of the fields for this record should have identical values to that of the "main" plate. The only field for the inset records that should have a different value than the main plate is the identifier value (identifier vs. identifier_inset1).


### Multiple-scale volumes

Historical urban atlases for densely populated cities are likely to include plates that are homogenous in scale.

On the other hand, it is common in atlases representing less densely-populated areas, like in county and town atlases, to find plates at various scales. When this occurs, separate mosaics should be created for each scale.

1. Within the working atlas root directory, create two sub-folders that will house the mosaic data for each scale mosaic. Use the barcode as the folder basename with alphabetic suffixes to differentiate between the scales:
  - example:  39999059011153a, 39999059011153b, and so forth for each scale that exists

2. Create a new record in the Airtable for each scale mosaic with the appropriate barcode ID

3. Proceed with the georeferencing process as normal. A separate footprint will also need to be created for each scale.

### Image files

In cases where you wish to download all image files associated with a particular BPL barcode, use [get-all-by-barcode.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/get-all-by-barcode.py "Download all tiffs script"). Resulting downloaded images will be named the file's BPL identifier.

In cases where you need to batch edit the file names of images, use [rename-files.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/rename-files.py "Rename files script").
