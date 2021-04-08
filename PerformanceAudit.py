import json
import requests
import datetime
import jmespath
import re
import streamlit as st
from bokeh.models.widgets import Div
import urllib.parse
#variables
API_JSON_FILENAME = "API_URL.json"
RESPONSE_FILENAME = "API_Response.json"
STATUS_FILENAME = "Status_Code.json"
TIME_FILENAME = "Elapsed_Time.json"
HEADER_FILENAME = "Response_Headers.json"
JMESPATH_STATUSCODE = 'locations[0].api'


# get database info
# def call_rest_api(searchJson, replaceString):
#     # Extract out the API url from json
#     searchApi = search_json['api', None]
#     print(searchApi)

    #return requests.get("https://" + searchApi).json()
#streamlit code
st.image('/Users/alexheinle/Desktop/SPAudit_Logo.png')
st.title('API Metric Results')
st.header('')




# write database info to file
def write_data_to_file(filename, filedata):
    with open(filename, 'w') as outfile:
        json.dump(filedata, outfile, indent=4, sort_keys=True)



# def write_time(timefile, timedata):
#     with open(timefile, 'w') as outfile:
#         file2 = open(timedata, outfile)

# def write_time(timefile, timedata):
#     with open(timefile, 'w') as f:
#         elapsedTime.elapsed = f
#         print(elapsedTime.elapsed)

#f = open("demofile2.txt", "w")
#f.write(elapsedTime.elapsed)






# opening config file and reading in API
with open('/Users/alexheinle/Desktop/Security&Performance Audit/Security-Performance-Audit/APIClient.json') as json_file:
    datain = json.load(json_file)
    # Get API URL from json
    API_URL = datain['locations'][0]
    print(API_URL)
    write_data_to_file(API_JSON_FILENAME, API_URL)
    # streamlit code for url
    st.header('URL')
    st.markdown('Below is the URL of the API')
    st.success(API_URL)


    # gets the API status code
    statusCode = 'http://127.0.0.1:5000/product/list/'
    #statuscode = call_rest_api(JSON_FILE, None)
    #statusCode = searchjson['api']
    api_Status = requests.get(statusCode)
    #statusCode = "http:" + statusCode
    print(api_Status.status_code)
    write_data_to_file(STATUS_FILENAME, api_Status.status_code)

    # streamlit code
    st.header('STATUS CODE')
    st.markdown('Below is the status code of the API. Status codes indicate whether the HTTP request has been successfully completed. The responses are grouped into 5 different categories.  Click the checkbox below to learn more.')
    st.success(api_Status.status_code)

    if st.checkbox('Learn More About Status Codes'):
        st.markdown('Below are the 5 groupings of status codes.')
        st.image('/Users/alexheinle/Desktop/statuscode2.png')
        st.write("[Click here to find the reason behind your status code response](https://httpstatuses.com/)")







    # gets the elapsed time of the request to the arrival of response
    time = 'http://127.0.0.1:5000/product/list/'
    elapsedTime = requests.get(time)
    print(elapsedTime.elapsed)
    #elapsedTime.elapsed = datetime.timedelta(seconds=24*60*60)
    #timedelta_seconds = elapsedTime.elapsed.total_seconds()
    #print(timedelta_seconds)
    f = open("ElapsedTime.txt", "w")
    f.write(str(elapsedTime.elapsed))
    #write_data_to_file(TIME_FILENAME, elapsedTime.elapsed)

    # streamlit code
    st.header('ELAPSED TIME')
    st.markdown('Below is the time it took from the start of the call to the response of the API.  The elapsed time is a good way to measure the performance of your API.')
    st.success(elapsedTime.elapsed)
    if st.checkbox('Learn More About API Performance'):
        st.write("[Click here to find the out how to improve your performance](https://nordicapis.com/making-fast-apis-lessons-learned-from-40-years-of-sql/)")
        st.image('/Users/alexheinle/Desktop/responsetime2.png')


    response_headers = 'http://127.0.0.1:5000/product/list/'
    response = requests.get(response_headers)
    print(response.headers)
    f = open("Response_Headers.json", "w")
    f.write(str(response.headers))

    # streamlit code
    st.header('RESPONSE HEADERS')
    st.markdown('Below is the response headers of the API')
    st.success(response.headers)

    # gets API response in JSON FORMAT
    response = 'http://127.0.0.1:5000/product/list/'
    a = requests.get(response)
    print(a.json())
    write_data_to_file(RESPONSE_FILENAME, a.json())

    # streamlit code
    st.header('RESPONSE')
    st.markdown('Below is the response of the API in json format')
    st.write(a.json())

    #adding flask dashboard
    st.header('REQUEST DASHBOARD')
    st.markdown('Click the button below to see an API dashboard of metrics such as method distribution and request count by time.')
    url = 'http://127.0.0.1:5000/flask-profiler/'
    #url = 'http://127.0.0.1:5000/api/v1/resources/books?author=Connie+Willis/flask-profiler'

if st.button('Request Count by Time'):
    js = "window.open('http://127.0.0.1:5000/flask-profiler/')"  # New tab or window
    js = "window.location.href = 'http://127.0.0.1:5000/flask-profiler/'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
