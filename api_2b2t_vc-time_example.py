import json
import http.client
conn = http.client.HTTPSConnection("api.2b2t.vc")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
conn.request("GET", "/time", headers=headers)
response = conn.getresponse()
data = response.read()
conn.close()
data = json.loads(data)
last_updated = data['lastUpdated']
world_time = data['worldTime']
print(last_updated)
print(world_time)
