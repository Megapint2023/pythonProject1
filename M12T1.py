#Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

#import requests
#import json
#
#hakusana = 'cats'
#osoite = "https://api.tvmaze.com/search/shows?q=" + hakusana
#    vastaus = requests.get(osoite)
#    data = vastaus.json()
#
#    print(vastaus)
#    print(data)
#    print(json.dumps(data, indent=2))
#
#    for tv_show in data:
#        #print(show)
#       # print(['show'])
#        print(tv_show['show']['name'])
#        show = tv_show['show']
#        name = show['name']
#        print(show['name'])
#        print(name)


import requests
import json

osoite = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(osoite)
data = vastaus.json()

print(vastaus)
print(data)
print(json.dumps(data, indent=2))
print("Chuck Norris vitsi:", data["value"])