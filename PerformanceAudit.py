import json
import requests
#import jmespath
import re
#import urllib.parse

#variables
API_JSON_FILENAME = "APIData.json"

# get database info
def call_rest_api(searchJson, replaceString):
    # Extract out the API url from json
    searchApi = searchJson['api']

    if replaceString is not None:
        match = re.findall("___([^ _]+)___", searchApi)

        for list in match:
            print(list)
            # replace the keyword with the value
            old = "___" + list + "___"
            searchApi = re.sub(old, urllib.parse.quote(replaceString), searchApi)


    # Calling first API to get data information
    return requests.get("https://" + searchApi).json()


# write database info to file
def write_data_to_file(filename, filedata):
    with open(filename, 'w') as outfile:
        json.dump(filedata, outfile, indent=4, sort_keys=True)

# opening config file and reading in API
with open('/Users/alexheinle/Desktop/SPAudit/APIClient.json') as json_file:
    datain = json.load(json_file)

    dataout = {}
    dataout['main'] = []
    counter = 1

    out = {}
    out['ApiInfo'] = []

# Get all json needed for program
    sportSearchJson = datain['locations'][0]

# Getting json from response
    allApiJson = call_rest_api(sportSearchJson, None)
    print(sportSearchJson)

    # Method call to write to file
    write_data_to_file(API_JSON_FILENAME, None)



# add exit time to DB
