# California Jobs Schema
###**Exploring ALL California Job Classification Schemas!**

Exploratory project intended to make CalHR job classification data useful in parsed form; this will enable enhanced sorting, in-depth analysis, ladder analysis, cross-referencing, clustering and more.  

All collaboration is welcome, specifically re: pdf conversion to txt (see known issues), front end, sqlite db (tiny, ~10,000 rows), content copy

####**Currently:**
* Uses wget to download the most recent version of the alphabetic jobs classification schema
* Python parsing of all fields using string manipulation and export to txt, csv, etc.

####**Known Issues:**
* Requires consistent, automated way to convert PDF to raw text
 * Have considered xpdf, pdftotxt, ghostscript, ps2ascii; all work.. but text recognition formats are inconsistent, even without considering OCR
 * This is still a manual process as of this posting

####**Future Plans:**
* Cluster job classifications by schema, in order to demonstrate promotional opportunities by strict ladder classification
* Provide visual representation of job clusters and potential lateral promotions between distinct ladders
 * Potentially via python scikit-learn or scipy.cluster, GNU gephi
* Integrate schematic arrangement of classes via http://www.calhr.ca.gov/Pay%20Scales%20Library/PS_Sec_16.pdf
