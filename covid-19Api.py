import requests
import json

url = "https://covid-193.p.rapidapi.com/countries"

headers = {
    'x-rapidapi-key': "9f1fc68319msh11ded1625d27157p1e9ed9jsn2e301ec93204",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

#countries

print("countries")
#print(json.dumps(response.json(), indent = 4, sort_keys=True))

#statistics
url = "https://covid-193.p.rapidapi.com/statistics"
response = requests.request("GET", url, headers=headers)
print('statistics')
print(json.dumps(response.json(), indent = 4, sort_keys=True))

#history
url = "https://covid-193.p.rapidapi.com/history"
querystring = {"country":"bahrain","day":"2021-02-20"}

response = requests.request("GET", url, headers=headers, params=querystring)
print("################\n#######################\n#############################")

#print(json.dumps(response.json()))

latest=response.json()["response"]


print("################\n2222222222222222\n#############################")
print(json.dumps(latest, indent = 4, sort_keys=True))
