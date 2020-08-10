import datetime
import json
import requests
import http.client, urllib.parse

import key #make sure to create a new file called 'key.py' with the content: key='YOURTHINGSPEAKAPIWRITEKEY'
key = key.key

data1 = requests.get(url="http://localhost/admin/api.php")
jsonobj1 = json.loads(data1.content.decode('utf-8'))
dns_queries_today = jsonobj1["dns_queries_today"]
unique_domains = jsonobj1["unique_domains"]
ads_blocked_today = jsonobj1["ads_blocked_today"]
ads_percentage_today = jsonobj1["ads_percentage_today"]

print ('queries today:              '  +str(dns_queries_today))
print ('unique_domains:       '  +str(unique_domains))
print ('ads_blocked_today:    '  +str(ads_blocked_today))
print ('ads_percentage_today: '  +str(ads_percentage_today))


params = urllib.parse.urlencode({'field1': dns_queries_today, 'field2': unique_domains, 'field3': ads_blocked_today, 'field4': ads_percentage_today, 'key':key })
headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("api.thingspeak.com:80")
conn.request("POST", "/update", params, headers)
response = conn.getresponse()
print (response.status, response.reason)
data = response.read()
conn.close()
