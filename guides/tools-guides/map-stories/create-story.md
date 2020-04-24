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

<img src='https://geoservices.leventhalmap.org/docs/media/img/iiif-viewer.png'></img>

4. You should see the map pop up in this viewer. Hold Shift and drag around an area which you’d like to annotate in the next “step” of your map storyline. 

> The story viewer will automatically give you a bit of buffer on the bottom edge to account for the caption box, but you should still give a generous margin on the bottom side of your area.

5. If you need to adjust the box, shift and drag on one of its edges, or just shift and drag in a new place

<img src='https://geoservices.leventhalmap.org/docs/media/img/shift-drag.png'></img>

6. Copy the bracketed set of numbers in the table under “Extent Coordinates” (including the brackets themselves) 
7. Paste this string, with the brackets, into the extent column of the Google Sheet 
8. Note that zooming and panning on the Extent Viewer doesn’t have an effect on how your story will look. The story presentation tool will automatically zoom to fit the extent box which you’ve selected. 

### Add more maps or images and steps {docsify-ignore}

You can add a second “stop” on your map by adding a second row to the Google Sheet, and so on. If you use the same id but a new extent, it will be the same map zoomed to a different section. If you use a new id, you’ll be jumping over to a new map or image. 


### Publishing {docsify-ignore}

1. The “Map Story Generator” tool creates a map storyline from your Google Sheet. Open it in a new browser window or tab: https://geoservices.leventhalmap.org/map-story-generator/ 
2. Back in your Google Sheet, select the “Share” button, make sure that Link Sharing is “on,” and then copy the shareable link to your Google Sheet 
3. In the Map Story Generator tool, paste the shared link to your Google Sheet in the first box 
4. In the second box, “Tour Identifier,” choose an identifier for your story. This will become part of your tour’s URL, and it shouldn’t have spaces. For instance, if you choose “boston-public-garden” as your identifier, the final story will have the URL “https://geoservices.leventhalmap.org/map-stories/#boston-public-garden” 

>NOTE: If you choose the same identifier as an existing story, running this tool will UPDATE the story rather than creating a new one. This is how you edit an existing story. 

5. In the third and fourth boxes, type the name of your story and the author name. 
6. Click the “Generate” button, and, if everything goes correctly, you should get a map story URL created for you!  
7. Click through to the URL for the new story to see it live. If you need to make edits, go back to your Google Sheet, and then begin again at Publishing step 3 here, using the same “Tour Identifier” 

<div class = "considerations"> 
💡 <a href = "https://geoservices.leventhalmap.org/docs/#/guides/tools-guides/map-stories/how-it-works?id=making-updates" target = "_self">How do updates work? </a> 
</div> 