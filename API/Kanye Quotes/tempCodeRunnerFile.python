import requests

url = "https://rto-vehicle-details-rc-puc-insurance-mparivahan.p.rapidapi.com/api/super-vehicle-info"

querystring = {"vehicle_no":"TN63BV4748"}


headers = {
	"x-rapidapi-key": "73be45d676msh012c8e258cc48adp188179jsn852832fbfbb1",
	"x-rapidapi-host": "rto-vehicle-details-rc-puc-insurance-mparivahan.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())