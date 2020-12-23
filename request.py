import requests, json



url = 'http://localhost:5000/api/'



data = [[24.00, 68.10, 17.21]]


j_data = json.dumps(data)


headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

r = requests.post(url, data=j_data, headers=headers)

print(r,r.text)
print(r.json())


