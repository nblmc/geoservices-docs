# Creating the masking footprint

## Context

This step produces a **footprint** for the atlas. This footprint is a polygon layer used to:

1. Mask out superfluous or empty “white space” on historical atlas plates, a necessary step for seamless mosaicing
2. Store references to plate-level library metadata, ultimately included in front-facing interfaces for the purpose of increasing accessibility to the historical archives

Broadly, this is accomplished by:

1. Generating a polygon layer that includes a feature for every georeferenced plate in the atlas, and editing the geometry of these features to appropriately reflect the desired extent of the plate data (including insets)
2. Joining the newly created footprint with plate-level library metadata
3. Exporting the footprint in geoJSON format for use in front-facing discovery environments

## Tips

- Use the [libguide plate index](https://apps.bpl.org/nblmc/indexes/index-pinney-1861-boston.html "libguide plate index example"), or, if no libguide plate index exists, the [historical index plate](https://collections.leventhalmap.org/search/commonwealth:6h446z575 "historical index plate example") to determine which plates are adjacent to one another and warrant a comparison. <br>
*Prior to offering direct access to high-resolution mosaiced imagery, BPL provided vector plate indices to locate atlas plates by location. Conceptually and in format, these index guides resemble the footprint layer described by this step, but because these indices were created for the purpose of locating plates, and not for mosaicing, they lack the necessary degree of accuracy required to create high-quality mosaics.*

- To change image transparency, right-click the layer in the table of contents → Properties → Legend → use arrow to add opacity slider to Used Widgets. After clicking OK, slider will appear in layer list

- Properties → Transparency → **No Data** set to **0** removes the black border

- Make sure snapping is set to **Vertex and Segment**, and **Topological Editing and Snapping on Intersection** are **enabled**
Project → Snapping options

![Snapping](/media/img/snapping.png)


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



## Steps

### Plate geometry


1. Change the Airtable field “footprint” from “to do” to “in progress”

2. Make a copy of [create-plate-index.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/create-plate-index.py "script to autogenerate footprint layer") inside the folder containing the georeferenced images (spatial_imagery)

3. Open a terminal at the folder containing imagery by **right-clicking → New terminal at folder**

4. Run the following command:

```shell
$ python3 create-plate-index.py
```

5. Open QGIS

6. Add newly generated `atlas_root/spatial_imagery/index/index.shp` to map

> This is an index file that contains features with the extent of each georeferenced image. Each polygon corresponds to a record in the index attribute table, with the plate id name (e.g. 0001) as the value for field “identifier”. You will need to edit the boundaries/vertices of each polygon to create a masking footprint suitable for mosaicing.

7. Add the imagery of a feature that needs editing, along with imagery of adjacent plates, for comparison

8. Drag the index shapefile to the top of the layer list, so that it sits on top of the imagery, and adjust the transparency so the imagery is visible

9. Open the attribute table

10. Click on the pencil icon to toggle editing

11. Remove the .tif suffix from the identifier values, so that values are only the plate name

> **G1234_B6G475_S2_1867v1_0006.tif**  → becomes → **G1234_B6G475_S2_1867v1_0006**

12. Click the pencil & save the edits

13. Exit the attribute table

### Drawing & editing

1. Main document menu → toggle editing

2. Make sure snapping is set to **Vertex and Segment**, and **Topological Editing and Snapping on Intersection** are **enabled**
Project → Snapping options

![Snapping](/media/img/snapping.png)



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
![check-validity](/media/gif/check-validity.gif)

### Joining metadata


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
**Right click Boundary → Properties → Joins → Green Plus Sign (bottom left)**

> - Join Layer = **metadata**
> - Join field = **identifier**
> - Target field = **identifier**

10. Open the Boundary attribute table to make sure everything joined properly, and all of the values have populated


### Exporting footprint

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

10. Update the Airtable to reflect that the footprint has been completed, ensure that the footprint data is accessible on the Maps Drive for mosaicing, and if imagery is also completed, post "atlas short description ready to mosaic" to #atlascope-general slack channel. 


## Special Instructions

### Inset metadata

If your atlas contains insets:

1. In metadata.csv, copy the record that exists for the whole plate (e.g. if the inset is for `_0004_inset1`, copy record `_0004`)

2. Insert a new row in the spreadsheet with the copied values

3. In the identifier field for the new record you just created, add appropriate inset suffix

4. Every feature you have created or edited in the boundary file **needs to have a corresponding record in metadata.csv** for the one-to-one join to perform correctly

5. The only field where values should differ between insets and corresponding “main” plate (0004 vs. 0004_inset1) is the identifier field. All of the rest of the metadata should be the same.


### Missing plate properties

There may be some cases where the plate field is not included in the library metadata. This field **does** need to be included in Boundary.geojson. Follow these steps:

1. Create a copy of [get-plate-value.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/get-plate-value.py "get-plate-value.py") and place it inside the folder containing Boundary.geojson `atlas/footprint/Boundary.geojson`

2. Open a terminal at the folder containing imagery by **right-clicking → New terminal at folder**

3. Run the following command:

```shell
$ python3 get-plate-value.py
```
4. Follow the prompts, inspecting the plate values in the digital collections

5. Open Boundary.geojson in a text editor and ensure that the plate field was created, and values were populated correctly
