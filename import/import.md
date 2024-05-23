
### Import
This folder contains examples of scenarios for importing Power BI models to the service via the API.  The source pbix files for this can be found in the [files](../files/) directory.  Please note that NYCYellow model is stored as a pbit file which cannot be imported via the API.  To use this you'll first need to open the file in Power BI Desktop, refresh the model, and then save it as a pbix file before the import operation.


1. [Import Model Encoded Body](./ImportModel-EncodedBody.ipynb) - This illustrates how to import a pbix file as a multi-part encoded byte stream.
1. [Import Model Temporary Location](./ImportModel-TempLocation.ipynb) - This illustrates how to import a pbix file via a temporary blob location.
1. [Import Model Advanced](./ImportModel-Advanced.ipynb) - This illustrates the concept of examining the size of the file prior to import to determine the best method.