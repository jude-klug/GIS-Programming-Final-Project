# GIS-Programming-Final-Project
An ArcGIS custom Python tool created for a final project that utilizes census API to combine TIGER/Line shapefiles and census data.

Some precanned data is included in this note and in the "sampledata.gdb" folder. 

To use this tool you need 3 text inputs. These are components of the API call and this was the most convenient and streamlined way that worked for me. Below are the pre-prepared data for the inputs of the tool that can't be included in the geodatabase.

Census URL: https://api.census.gov/data/2023/acs/acs5/subject?get=
Census Columns: GEO_ID,NAME,S1501_C01_012E
UCGID: &ucgid=pseudo(0500000US41051$1400000)

Please take care to not include any additional spaces and copy and paste them exactly as they appear into the proper boxes. All other instructions will be in the tool.
