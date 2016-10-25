# California Jobs Schema
###**Exploring ALL California Job Classification Schemas!**
###**Big Update 2016-10-24!**
#### CA is looking to collaborate with citizens for this project!

##### CA is looking to build a database or other repository, containing the class data for all current classifications so that it can be searched, normalized, catalogued.
By doing this, we will be able to help qualified job seekers more easily discover what positions they are eligible for. For example, it will enable recent college graduates to see what jobs their degree makes them immediately eligible for! Also, it will aid as a career progression discovery tool, for lateral, diagonal and vertical movement, as well as a host of other benefits to making CA the most efficient state in the nation.

We need your help, specifically the skills needed for this phase will be: 

* XPATH or CSS selecting (language agnostic)
* **OPEN SOURCE** RDBS and/or NoSQL
* Natural Language Processing (NLP)
* Linked network analysis, key word in context, soundex, similarity score maybe tf-idf or cosine similarity (I'm not an expert in this area, suggestions happily accepted as an GitHub issue)

Other guiding principles:

* **Open source only**, yes Stata/MatLAB/SAS are great but this is public data and we want to make sure all citizens have access to it (but by all means use the FREE SAS Studio edition, R, Python, etc :)
* An **abstracted/generalized, automated solution**. We appreciate citizens getting their hands dirty in the data and manually brute forcing through it to help the state, but just imagine instead of ~1,800 class codes you have 1,800,000 or the text changes, would it still work?
* Contributed code is intended to help benefit the people of California, credit may be given but **anything submitted (including in issues) will be considered to be fully open source to the fullest extent of what "open source" may mean.**

----------------------------

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