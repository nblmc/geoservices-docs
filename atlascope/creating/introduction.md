# Introduction

The following guides will walk through a process that begins with a [collection of individual atlas plates](https://collections.leventhalmap.org/search?utf8=%E2%9C%93&q=39999059015550 "Cambridge 1873 plate list"), and results in a [mosaiced tiled map service](https://geoservices.leventhalmap.org/atlas-extent-viewer/index.html#39999059015550 "Cambridge 1873 mosaic").


The broad contours of this workflow include georeferencing individual atlas plates, masking them using a footprinting layer to only reveal appropriate data, stitching plates together to create a raster mosaic, and publishing the stitched mosaic as a tiled map service.


Some instructions pertain to particulars of the Leventhal Map & Education Center (LMEC) at the Boston Public Library (BPL) collections, for example, file naming structures, metadata standards, and so on, but the idea behind and implementation for each step can be applied universally. *BPL-specific instructions will be flagged, to indicate one should consider their own institution or project-specific details.*

The software and tools described in this process are all free. Cost lies in staff time required to process the imagery, and in data storage for resulting tile services.


The guides for each step in the process have been written to include context, tips for efficiency (e.g. when adding a control point in QGIS, hold the spacebar to pan the map), step-by-step instructions for working through the process, and any special notes or considerations.

A workflow for mosaicing historical atlases could take many different forms. Please find included the one we have discovered - through trial and error - works best for creating low-cost, high-quality tiled map services of historical atlas mosaics in open formats. This workflow relies on the use of QGIS and free-standing Python scripts in a Mac environment. Please do not hesitate to get in touch for further inquiry, or for help navigating special considerations centered on the use of Windows or the ESRI suite: *reference@leventhalmap.org*
