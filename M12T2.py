# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen
# ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen,
# jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
# U: playtime1945
# P: strong
# @: metropolia
# API:


import requests
import json

hakusana = input("Anna paikkakunta: ")
api_key = "543cd516ab7095dab8faac0cf1a3731d"

pyyntö = "https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid={api_key}"
vastaus = requests.get(pyyntö)
data = vastaus.json()

print(vastaus)
print(data)
print(json.dumps(data, indent=2))