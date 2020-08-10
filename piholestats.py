import datetime
import json
import requests
import http.client, urllib.parse

import key #make sure to create a new file called 'key.py' with the content: key='YOURTHINGSPEAKAPIWRITEKEY'
key = key.key

data1 = requests.get(url="http://localhost/admin/api.php")
jsonobj1 = json.loads(data1.content.decode('utf-8'))
queries = jsonobj1["dns_queries_all_types"]
print (queries)

params = urllib.parse.urlencode({'field1': queries, 'key':key })
headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("api.thingspeak.com:80")
conn.request("POST", "/update", params, headers)
response = conn.getresponse()
print (response.status, response.reason)
data = response.read()
conn.close()
