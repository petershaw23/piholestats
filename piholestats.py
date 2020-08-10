import json
import urllib2
 
try:
    f = urllib2.urlopen('http://localhost/admin/api.php')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    queries = parsed_json['dns_queries_today']
    adsblocked = parsed_json['ads_blocked_today']
    clients = parsed_json['unique_clients']
    f.close()
except:
    queries = '-'
    adsblocked = '-'
    clients = '-'
 
pihole = 'DNS-Queries: ' + str(queries) + ' - ' + 'Ads blocked: ' + str(adsblocked) + ' - ' + 'Devices: ' + str(clients)
print (pihole)
