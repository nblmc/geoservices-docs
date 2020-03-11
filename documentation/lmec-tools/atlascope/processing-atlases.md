# Introduction {docsify-ignore}

The LMEC collection of fire insurance and real estate atlases of metropolitan Boston is in the process of being imaged, georeferenced, and mosaiced to produce continuous-coverage, geographically-locatable versions of these historic objects.

This documentation contains information on how to create the underlying data sources of the Atlascope project, including raster imagery, vector boundary files, and metadata records. It assumes prior knowledge with GIS and data tools, and is written for a Mac + QGIS environment. For questions related to Windows or ESRI workflows, please do not hesistate to [get in touch](leventhalmap.org/research/gis "gis form").

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

The various scripts and processes in this project generate many temporary working files that are worked with and stored locally. There is a backup strategy in place for data that should be archived long-term:

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


# Masking footprint

Footprint layers are used to mask out superfluous or empty “white space” on historical atlas plates, a necessary step for seamless mosaicing. Once created, these layers are joined with bibliographic metadata and used to store references to plate-level information. This facilitates collections-discovery functionalities of the front-facing tools, particularly the ability to link back to unique items in the digital collections. 

This process is accomplished by auto-generating a masking polygon layer that includes a feature for every georeferenced plate in the atlas, and hand-editing the geometry of these features to appropriately reflect the desired extent of each plate's historical coverage. 


[Create-plate-index.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/create-plate-index.py "script to autogenerate footprint layer") will create a new polygon layer with a feature for each plate, and a value in the attribute table for that plate's identifier number. This identifier number is the common field used to join with metadata, and also to accomplish the masking. 

Step-by-step masking instructions are available in [create mosaics → masking](#/guides/tools-guides/atlascope/create-mosaics?id=masking "create mosaics guide").


**Snapping:**
Snapping is set to **Vertex and Segment**, and **Topological Editing and Snapping on Intersection** are **enabled**
Project → Snapping options


# Joining metadata 


<details>
<summary>Note on BPL metadata particulars</summary>

> - The instructions to join features to library metadata are specific to the ways BPL creates, manages & and stores metadata for its maps<br>
> - These instructions can be applied to other metadata configurations -- the key is that there needs to be a field common to the polygon footprint layer and the bibliographic metadata table for each unique atlas plate in order to complete a one-to-one join between the polygon layer and the tabular metadata table <br>
> - BPL uses the **identifier** field for this join. Joining this polygon layer where each feature represents the geographic extent of a collections item to library metadata increases accessibility to the historical collections items within the context of map-based discovery interfaces<br>

</details>

>**Fields to preserve and naming conventions:** <br><br>
→ identifier <br>
→ call_no <br>
→ commonweal <br>
→ title <br>
→ plate <br>
→ publisher <br>
→ year


>**Export settings for the <span style="background-color:#75b79e;color:white;">masking</span> version of footprint layer:** <br><br>
→ Format = **GeoJSON** <br>
→ Destination path = `atlas_root/footprint/Masking.geojson` <br>
→ CRS: **EPSG 3857 - WGS 84 / Web Mercator** <br>


>**Export settings for the <span style="background-color:#75b79e;color:white;">collections discovery</span> version of footprint layer:**<br><br>
→ Format = **GeoJSON** <br>
→ Destination path = `atlas_root/footprint/Boundary.geoJSON` <br>
→ CRS: **EPSG 4326 - WGS 84** <br>



# Null plate value

There may be some cases where the plate field is not included in the library metadata. [Get-plate-value.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/get-plate-value.py "get-plate-value.py") run from inside the folder containing Boundary.geoJSON will locate these values and place them in the Boundary JSON.

# Mosaic.py

[mosaic.py](https://github.com/nblmc/atlascope-assets/blob/master/scripts/mosaic.py "mosaicing script") iterates through each georeferenced atlas plate and masks that plate to the hand-drawn geometry of the corresponding boundary feature in the footprint layer. The masked geotifs, after being compressed and going through various imagery setting adjustments, will then be mosaiced. The output of running this tool is a large, stitched geotif for the atlas.

If all of the data has been prepared correctly, this tool should work without issues.
If errors are returned, the mosaic will not generate, and you will need to use the error messages to debug issues with the input geoTIFF and footprint data.


# TMS Tiling

Tiles are created using gdal2tiles.py. The command is run from `Documents → temp-atlas-tiles → barcode → mosaic.py`. Tiles are uploaded to cloud storage, backed up to [appropriate storage](#/documentation/lmec-tools/atlascope/processing-atlases?id=file-backup "storage"), and the local tiles are erased. 

```shell
$ gdal2tiles.py -r cubic -p mercator -e -z 13-20 --processes=6 mosaic.tif tiles/
```
gdal2tiles.py creates .png tiles for a perfect rectangle around the map mosaic, including areas which do not have any imagery data. Empty tiles should be deleted by running the following command from the tiles directory:

```shell
$ find . -type f -size -335c -delete
```


# Cloud upload

Tiles are pushed to Wasabi cloud storage via s3cmd. 
s3cmd can be installed using `brew install s3cmd` and configuring our Wasabi credentials by following the steps [here](https://wasabi-support.zendesk.com/hc/en-us/articles/115001757791-How-do-I-use-s3cmd-with-Wasabi- "here")

Once s3cmd is configured, run the following command from the tiles directory:

```shell
$ for i in {13..20}; do cd $i; for f in *; do s3cmd put --recursive $f s3://urbanatlases/BARCODE/tiles/$i/; done; cd ../; done
```

