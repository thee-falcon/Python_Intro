import requests
import config

url = "https://docs.developer.yelp.com/"

headers = {
    "Autorization": "Bearer " + config.api_key
}
params = {
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [businesses["name"] for business in businesses if business["rating"] > 4.5]
print(names)