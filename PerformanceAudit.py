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

    # Get API URL from json
    API_URL = datain['locations'][0]

    # Getting json from response
    allApiJson = call_rest_api(API_URL, None)
    print(API_URL)

    # Method call to write to file
    write_data_to_file(API_JSON_FILENAME, API_URL)



# add exit time to DB
