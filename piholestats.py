import datetime
import json
import requests
import http.client, urllib.parse
data1 = requests.get(url="http://localhost/admin/api.php")
jsonobj1 = json.loads(data1.content.decode('utf-8'))
queries = jsonobj1["dns_queries_all_types"]
print (queries)
