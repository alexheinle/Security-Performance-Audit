import json
import requests
import jmespath
import re
#import urllib.parse
try:
    from urllib.parse import urlparse
except ImportError:
    import urllib as urlparse
     #from urlparse import urlparse
article_JSON_FILENAME = "articleData.json"
#ARTICLE_FILENAME = "articleData.json"
PLAYER_ATTRIBUTES = 'parameters[0].values'
# print(type(PLAYER_ATTRIBUTES))


def call_rest_api(searchJson, replaceString):
    # Extract out the API url from json
    searchApi = searchJson['api']
    print(searchApi)

    #if replaceString is not None:
        #match = re.findall("___([^ _]+)___", searchApi)

        #for list in match:
            #print(list)
            # replace the keyword with the value
            #old = "___" + list + "___"
            #searchApi = re.sub(old, urlparse.quote(replaceString), searchApi)
                                #urllib.parse.quote

    # Calling first API to get article information
    return requests.get("https://" + searchApi).json()


def search_json(searchCriteria, json):
    # print(type(searchCriteria))
    # searchCriteria = {}
    # json = {}
    searchResult = jmespath.search(searchCriteria, json)
    return searchResult

def write_data_to_file(filename, filedata):
    with open(filename, 'w') as outfile:
        json.dump(filedata, outfile, indent=4, sort_keys=True)


with open('APIData.json') as json_file:
    datain = {}
    datain = json.load(json_file)
    print(datain)

    dataout = {}
    dataout['main'] = []
    counter = 1

    out = {}
    out['articleInfo'] = []
    #print(out)

    # Get all json needed for program
    sportSearchJson = {}
    sportSearchJson = datain['locations'][0]
    #locationSearchJson = datain['locations'][1]
    # print(sportSearchJson)
    # THIS IS A DICTIONARY


    # Getting json from response
    allarticleJson = call_rest_api(sportSearchJson, None)
    # print(allarticleJson)
    # this is a dictionary
    # aSourceDictionary = { 'abc' : [1,2,3] , 'ccd' : [4,5] }
    # dict = {}
    # for a in allarticleJson:
    #     if a not in dict:
    #         dict[a] = []
    #         dict[a].extend(allarticleJson[a])

    # Getting article attributes from original JSON
    articleAttributesQuery = search_json(PLAYER_ATTRIBUTES, sportSearchJson)
    # print(type(articleAttributesQuery))
    # these are the values we have stored in the config file
    # THIS IS A LIST

    # Search response json for attributes
    articleData = search_json(articleAttributesQuery, allarticleJson)
    # THIS IS A LIST
    print(articleData)


    # Getting json from response
    #allLocationJson = call_rest_api(locationSearchJson, articleData[1])

    # Getting article attributes
    #locationAttributesQuery = search_json(PLAYER_ATTRIBUTES, locationSearchJson)


    # Search response json for attributes
    #locationArticleData = search_json(locationAttributesQuery, allLocationJson)
    #print(locationArticleData)

    write_data_to_file(article_JSON_FILENAME, articleData)

    #write_data_to_file(ARTICLE_FILENAME, locationArticleData)
