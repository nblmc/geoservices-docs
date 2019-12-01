# Mosaicing

## Context

In order for individual atlas plates to be combined into a seamless mosaic, they must first be masked, using the footprint boundary layer, to show only relevant map data.

This step involves running a tool that will iterate through each georeferenced atlas plate and mask it to the geometry of the polygon feature in the Boundary footprint layer with the same identifier name. The masked rasters, after being compressed and going through various imagery setting adjustments, will then be mosaiced. The output of running this tool is a large tif file containing the mosaic for the atlas.

If all of the data has been prepared correctly, this tool should work without issues.
If errors are returned, the mosaic will not generate, and you will need to use the error messages to debug issues with the input geoTIFF and footprint data.

## Tips

> You will need to be able to run standalone Python scripts and utilize osgeo tools from the terminal in order to work through this step. Please find documentation on how to [configure a mac](https://geoservices.leventhalmap.org/docs/#/computing/mac-setup "Mac Setup") to these settings. If you wish to configure your Windows environment for this workflow, please do not hesitate to get in touch at reference@leventhalmap.org

## Steps

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
