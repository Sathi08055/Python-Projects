import requests

url = "https://quotes15.p.rapidapi.com/quotes/random/?language_code=en"

headers = {
    "x-rapidapi-host": "quotes15.p.rapidapi.com",
    "x-rapidapi-key": "73be45d676msh012c8e258cc48adp188179jsn852832fbfbb1"
}

response = requests.get(url, headers=headers)

data=response.json()
author=data["originator"]["name"]
quote=data["content"]
print(quote, author)
