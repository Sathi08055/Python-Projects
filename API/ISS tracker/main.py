import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")
data=response.json()
longitude=float(data['iss_position']['longitude'])
latitude=float(data['iss_position']['latitude'])
print(f"{longitude=}\n{latitude=}")