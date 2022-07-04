import requests

url = "https://www.hpb.health.gov.lk/api/get-current-statistical"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

with open("Coviddata.json",'w') as f:
    f.write(response.text)

