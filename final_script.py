
import arcpy, csv, requests
# establish variables

keyfile = arcpy.GetParameterAsText(0) # .txt file of api code
outfile = 'data.csv' # output exported census data, default placeholder name
censusfile = arcpy.GetParameterAsText(1) # beginning of url for census data
getcolumns = arcpy.GetParameterAsText(2) # columns included in the api query, optional
ucgid = arcpy.GetParameterAsText(3) # unique census area identifier, optional
tl = arcpy.GetParameterAsText(4) # tiger line census tract
study_area = arcpy.GetParameterAsText(5) # final output area clip, optional
results = arcpy.GetParameterAsText(6) # output name and location of the final data
GEOIDFQ = arcpy.GetParameterAsText(7) # field name on tiger/line shapefile
GEO_ID = arcpy.GetParameterAsText(8) # field name on join table


# Read API key and URL components
with open(keyfile) as key:
    api_key = key.read().strip()

data_url = censusfile + getcolumns + ucgid
data_url = data_url.strip()

response = requests.get(data_url)
popdata = response.json()

# Save to CSV
with open(outfile, 'w', newline='') as writefile:
    writer = csv.writer(writefile, quoting=csv.QUOTE_ALL, delimiter=',')
    writer.writerows(popdata)

# Convert CSV to table
csv_table = arcpy.management.MakeTableView(outfile, "csv_table").getOutput(0)

# Attempt to join
try:
    arcpy.management.JoinField(tl, GEOIDFQ, csv_table, GEO_ID)
except Exception as e:
    print(arcpy.GetMessages())
    arcpy.AddMessage('Something went wrong, please check your inputs and try again.')
    raise e
# Check spatial references
tl_sr = arcpy.Describe(tl).spatialReference
sa_sr = arcpy.Describe(study_area).spatialReference

if tl_sr.name == sa_sr.name:
    cc = arcpy.analysis.Clip(tl, study_area, results)
else:
    arcpy.AddMessage('Spatial references do not match. Please project your data first.')

# select and delete empty joined rows
select = arcpy.management.SelectLayerByAttribute(cc, "NEW_SELECTION", f"{GEO_ID} = ' '")
arcpy.management.DeleteRows(select)

arcpy.AddMessage('Tool completed successfully!')
