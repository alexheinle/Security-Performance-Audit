import json
import requests
#import jmespath
import re
#import urllib.parse
#variables
API_JSON_FILENAME = "API_URL.json"
RESPONSE_FILENAME = "API_Response.json"
STATUS_FILENAME = "Status_Code.json"
# get database info
def call_rest_api(searchJson, replaceString):
    # Extract out the API url from json
    searchApi = searchJson['api']

    return requests.get("https://" + searchApi).json()



# write database info to file
def write_data_to_file(filename, filedata):
    with open(filename, 'w') as outfile:
        json.dump(filedata, outfile, indent=4, sort_keys=True)





# opening config file and reading in API
with open('/Users/alexheinle/Desktop/SPAudit/test/APIClient.json') as json_file:
    datain = json.load(json_file)
    # dataout = {}
    # dataout['main'] = []
    # counter = 1
    # out = {}
    # out['ApiInfo'] = []

    # Get API URL from json
    API_URL = datain['locations'][0]

    print(API_URL)

    write_data_to_file(API_JSON_FILENAME, API_URL)


    # gets API response in JSON FORMAT
    response = 'http://newsapi.org/v2/top-headlines?q=Coronavirus&country=us&apiKey=0b179f0aeb954161bdefa27816db8bb4'
    a = requests.get(response)
    print(a.json())
    write_data_to_file(RESPONSE_FILENAME, a.json())

    # gets the API status code
    statusCode = 'http://newsapi.org/v2/top-headlines?q=Coronavirus&country=us&apiKey=0b179f0aeb954161bdefa27816db8bb4'
    api_Status = requests.get(statusCode)
    print(api_Status.status_code)
    write_data_to_file(STATUS_FILENAME, api_Status.status_code)
