import requests
import json

url = 'https://api.scryfall.com/catalog/enchantment-types'
url2 = 'https://api.scryfall.com/catalog/spell-types'
url3 = 'https://api.scryfall.com/catalog/keyword-abilities'
url_custo = 'https://api.scryfall.com/cards/search?q=c%3Awhite+mv%3D2'

response = requests.get(url_custo)
listening = response.json()
print(json.dumps(listening, indent=4, sort_keys=True))
