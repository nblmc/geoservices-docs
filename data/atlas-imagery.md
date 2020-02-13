# Using Digitized Urban Atlases as Data Sources

## About Urban Atlases

Info about atlases, atlascope, etc here ...

### Metadata and Object ID for Atlases

This Airtable lists all atlases which have been fully completed and appear in Atlascope.

<iframe class="airtable-embed" src="https://airtable.com/embed/shrBBu5AEseJvTjk5?backgroundColor=cyan&viewControls=on" frameborder="0" onmousewheel="" width="100%" height="533" style="background: transparent; border: 1px solid #ccc;"></iframe>

The `barcode` field is used as the stable identifier for a single atlas. It is derived from the object barcode attached to each physical item in the LMEC collections.

!> **Atlases with multiple scale factors.** Some single atlases include overlapping coverage of an area at multiple scales—for instance, the 1874 Hopkins atlas of Newton. These are treated as distinct digital atlas objects. We use alphabetical suffixes to create new id numbers for these atlases that derive from the same original physical item, as in 39999059015832a and 39999059015832b for the Newton atlas.



### URL Schema for Access to Digitized Atlases

#### TMS Tile Pyramid

A TMS tile pyramid at zoom levels 13 through 20 is available at the following source. Note that our tile system uses the OSGeo TMS spec, which uses an inverted Y coordinate compared to the XYZ system now used by most web map libraries. Therefore, passing `-y` is necessary to flip TMS to XYZ; see [this gist](https://gist.github.com/tmcw/4954720) for more information about the differences between TMS and XYZ.

```
https://s3.us-east-2.wasabisys.com/urbanatlases/{{ATLAS-ID}}/tiles/{z}/{x}/{-y}.png
```

#### Full Coverage GeoTIFF

A fully georeferenced and mosaiced GeoTIFF of a single atlas's full coverage can be found using this URL schema. Note that, because the different plates which constitute an atlas are oftentimes at different original scales, the full coverage TIFF does not have a strictly even DPI resolution relationship with the original, single-plate archival TIFFs. **These are very large files!**


```
https://s3.us-east-2.wasabisys.com/urbanatlases/{{ATLAS-ID}}/src/mosaic/mosaic.tif
```

#### Plate Boundaries Outline

This GeoJSON file represents the outlines of plate boundaries as vector polygons. Geometry has been simplified for computational efficiency in Atlascope.

```
https://s3.us-east-2.wasabisys.com/urbanatlases/{{ATLAS-ID}}/src/footprint/Boundary.geojson
```