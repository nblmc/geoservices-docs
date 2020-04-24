# Map Stories Instructions {docsify-ignore}

Map Stories are lightweight, interactive interpretive overlays on our Digital Collections. They are best for annotating zoomed-in sections of one or more maps. 

## To make a Map Story... {docsify-ignore}

### You will need: {docsify-ignore}
1. A browser tab open to our [Digital Collections portal](https://collections.leventhalmap.org/ "Digital Collections portal") and/or [Digital Commonwealth](https://www.digitalcommonwealth.org/ "Digital Commonwealth")  <br>
2. A browser tab open to the [IIIF Extent Viewer tool](https://geoservices.leventhalmap.org/iiif-extent-viewer/ "IIIF Extent Viewer tool")  <br> 
3. A Google Sheet; make a copy of [this template](https://docs.google.com/spreadsheets/d/1oe9omQd62_WSQiV7o8WOZPawB2oNEwabAmrOxYTs0gE/edit?usp=sharing "this template"). Each row needs information about what map/image to show, and what part (“extent”) to show, along with a caption. 

<div class = "considerations"> 
💡 <a href = "https://geoservices.leventhalmap.org/docs/#/guides/tools-guides/map-stories/how-it-works?id=iiif" target = "_self">What is IIIF? </a> 
</div> 

### Pick out your first map or image: {docsify-ignore}
1. Using the Digital Collections search tool, navigate to the record page for the first map you want to use <br> 
2. You’ll need to copy the part of the URL in your browser that looks like **commonwealth:abc123xyz**

<img src='https://geoservices.leventhalmap.org/docs/media/img/identifier-dc.png'></img>


3. Go to your Google Sheet, and in the first row, in the id column, paste that same string. <br>
4. For items in the LMEC digital collections, the repo field should be ‘lmec’. For items in Digital Commonwealth, the repo field should be ‘dc’. <br>
5. As of now, you should just enter the number 0 in the sequence field, for every row. 



<div class = "considerations"> 
💡 <a href = "https://geoservices.leventhalmap.org/docs/#/guides/tools-guides/map-stories/how-it-works?id=repo" target = "_self">Why do we specify which repo? </a> 
</div> 
<div class = "considerations"> 
💡 <a href = "https://geoservices.leventhalmap.org/docs/#/guides/tools-guides/map-stories/how-it-works?id=sequence" target = "_self">What is the sequence field for? </a> 
</div> 
  


### Decide which section of the map or image you’re going to use {docsify-ignore}

1. If you just want to show the entire map or image, just enter the word fit in the column extent of your Google Sheet 
2. If you want this stop on the storyline to show a zoomed in section of the map, go to the IIIF Extent Viewer tool in another tab.  
3. Paste the id string for your map into the “Enter Digital Commonwealth ID” field of the Extent Viewer, and click “Load” 

<img src='https://geoservices.leventhalmap.org/docs/media/img/iiif-.png'></img>