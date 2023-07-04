import requests
import json

site=requests.get("https://jsonplaceholder.typicode.com/todos")
dönüş=json.loads(site.text)
for i in dönüş:
    print(i["title"])