# Tiles


## Creating

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



10. At the beginning of the tile generation process, mosaic.tif was copied directly into the `Documents/atlas-temp-tiles/barcode` folder, in order to generate tiles at the correct local directory level. Drag mosaic.tif into `CLIRSTORAGE/barcode/src/mosaic` to permanently store the mosaic TIFF in the src folder.

## Sharing

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
