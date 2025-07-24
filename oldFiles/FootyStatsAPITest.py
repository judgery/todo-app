import requests
import json

r = requests.get('https://api.football-data-api.com/league-players?key=example&league_id=1625&page=3')
r.json()

json_file = json.dumps(r.json(), indent=4)

with open("players3.json", "w") as outfile:
    outfile.write(json_file)

# print(r.json())