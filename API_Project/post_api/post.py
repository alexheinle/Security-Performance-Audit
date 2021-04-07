import requests
import json

url="http://example.com/index.php"

r = requests.post('http://example.com/index.php', params={'q': 'raspberry pi request'})

if r.status_code != 200:
  print "Error:", r.status_code

#data = json.loads(r.text)
example = r["value1"]["value2"]
print(example)
