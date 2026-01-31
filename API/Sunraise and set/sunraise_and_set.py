import requests
import json
parameters = {
    "lat": 9.85,
    "lng": 78.47
}

response = requests.get(url="https://api.sunrisesunset.io/json", params=parameters)

# To see the actual data
data=response.json()
with open("file.json","w+") as file:
    json.dump(data,file,indent=4)


