import requests
import json

hakusana = 'cats'
osoite = "https://api.tvmaze.com/search/shows?q=" + hakusana

try:

    vastaus = requests.get(osoite)
    data = vastaus.json()

    print(vastaus)
    print(data)
    print(json.dumps(data, indent=2))

    for tv_show in data:
        #print(show)
       # print(['show'])
        print(tv_show['show']['name'])
        show = tv_show['show']
        name = show['name']
        print(show['name'])
        print(name)

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")