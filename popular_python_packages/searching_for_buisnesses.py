import requests

url = "https://docs.developer.yelp.com/"
api_key = "you can find one in yelp.com when you register"
headers = {
    "Autorization": "Bearer " + api_key
}
params = {
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [businesses["name"] for business in businesses if business["rating"] > 4.5]
print(names)