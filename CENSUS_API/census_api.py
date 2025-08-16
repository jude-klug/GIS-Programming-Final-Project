import requests, csv, json


keyfile = 'census_key.txt' # api code file
outfile = 'data.csv' # name of the exported .csv
censusfile = 'census_data.txt' # start of url for census data
get_columns = 'GEO_ID,NAME,S1501_C01_012E' #name of columns to extract
ucgid = '&ucgid=pseudo(0500000US41051$1400000)' # unique census area identifier (optional)

# read api key in from file
with open(keyfile) as key:
    api_key = key.read().strip()

# read census api url
with open(censusfile) as key:
    census_file = key.read().strip()

data_url = census_file + get_columns + ucgid
    
    
# retrieve data, print output to screen
response = requests.get(data_url)
popdata = response.json()
for record in popdata:
    print(record)

# write data to csv
with open(outfile, 'w', newline='') as writefile:
    writer = csv.writer(writefile, quoting=csv.QUOTE_ALL, delimiter=',')
    writer.writerows(popdata)
