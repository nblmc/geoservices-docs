# Using Digitized Urban Atlases as Data Sources

## About Urban Atlases


The LMEC collection of fire insurance and real estate atlases of metropolitan Boston is in the process of being imaged, georeferenced, and mosaiced to produce continuous-coverage, geographically-locatable versions of these historic objects. 

For more background on urban atlases, see the library research guides for [Boston](http://guides.bpl.org/urban-atlases) or [other Massachusetts cities and towns](https://guides.bpl.org/mass-urban-atlases). To learn more about the Atlascope public discovery tool, [read the documentation](https://geoservices.leventhalmap.org/docs/#/documentation/lmec-tools/atlascope/using-the-portal) or [try the app](https://atlascope.leventhalmap.org).

This documentation contains information on how to access the underlying data sources of the Atlascope project, including raster imagery, vector boundary files, and metadata records. It assumes prior knowledge with GIS and data tools.

## Identifying Atlases and their Metadata

### Tabular List of Atlases

This Airtable lists all atlases which have been fully completed and appear in Atlascope.

<iframe class="airtable-embed" src="https://airtable.com/embed/shrBBu5AEseJvTjk5?backgroundColor=cyan&viewControls=on" frameborder="0" onmousewheel="" width="100%" height="533" style="background: transparent; border: 1px solid #ccc;"></iframe>

The `barcode` field is used as the stable identifier for a single atlas. It is derived from the object barcode attached to each physical item in the LMEC collections.

!> **Atlases with multiple scale factors.** Some single atlases include overlapping coverage of an area at multiple scales—for instance, the 1874 Hopkins atlas of Newton, which includes both [small-scale plates covering built-up areas](https://atlascope.leventhalmap.org/#view:share$base:000$overlay:39999059015832a$zoom:14.23$center:-7926719.238595215,5213651.889357576$mode:glass$pos:483) as well as [large-scale plates covering the entire town](https://atlascope.leventhalmap.org/#view:share$base:000$overlay:39999059015832a$zoom:14.23$center:-7926719.238595215,5213651.889357576$mode:glass$pos:483). Because of their overlapping extent, these are treated as distinct digital atlas objects. We use alphabetical suffixes to create new id numbers for these atlases that derive from the same original physical item, as in 39999059015832a and 39999059015832b for the Newton atlas.

Atlases are colloquially referred to by the `desc_short` field, a concatenation of the atlases's primary coverage area and its year of publication—"Charlestown 1892," for instance. 

!> **Idiosyncracies in coverage areas**. The title and descriptive name of a single atlas can be deceiving. For instance, "Chelsea 1896" also covers Revere, Winthrop, and East Boston. Furthermore, as towns and cities have been annexed into Boston, or had their municipal lines adjusted, coverage areas have changed over time. Both the title and the descriptive name should not be used as an authoritative description of a single atlas's exact coverage extent.

The `bibliocommons` entry links to the atlas's record in the BPL's public access catalog, where a MARC record and other bibliographic detail is available.

### Spatial List of Atlases

A single GeoJSON file with polygons corresponding to each atlas's coverage extent can be found at the following URL. ([See here](https://github.com/nblmc/atlascope-assets/blob/master/atlas-footprints/volume-extents.geojson) for the file preview in GitHub.)

```
https://raw.githubusercontent.com/nblmc/atlascope-assets/master/atlas-footprints/volume-extents.geojson
``` 

This file is derived from the Airtable embedded above, and each polygon feature in this GeoJSON coverage contains metadata fields corresponding with the same fields in the Airtable record.

## URL Schema for Access to Digitized Atlases

To access the data associated with a single atlas, you will need to begin with the `barcode` field, which serves as the stable identifier in our data bucket.

### TMS Tile Pyramid

A TMS tile pyramid at zoom levels 13 through 20 is available at the following schema.

```
https://s3.us-east-2.wasabisys.com/urbanatlases/{{barcode}}/tiles/{z}/{x}/{-y}.png
```

!> **TMS vs XYZ**. Our tile pyramid is generated to the OSGeo TMS spec, which uses an inverted Y coordinate compared to the XYZ system now used by most web map libraries. Therefore, passing `-y` is necessary to flip TMS to XYZ; see [this gist](https://gist.github.com/tmcw/4954720) for more information about the differences between TMS and XYZ.

### Full Coverage GeoTIFF

A fully georeferenced and mosaiced GeoTIFF of a single atlas's full coverage can be found using this URL schema.

```
https://s3.us-east-2.wasabisys.com/urbanatlases/{{barcode}}/src/mosaic/mosaic.tif
```

!> These are very large files. Expect long download times.

!> **DPI compared to original imagery**. Because individual atlases plates are drawn at varying geographic scales, when they are combined into a single mosaic, they require different DPI adjustments. For this reason, some sections of a single atlas may have lossier transformations than others.

### Plate Boundaries Outline

This GeoJSON file represents the outlines of plate boundaries as vector polygons. Geometry has been simplified for computational efficiency in Atlascope.

```
https://s3.us-east-2.wasabisys.com/urbanatlases/{{barcode}}/src/footprint/Boundary.geojson
```