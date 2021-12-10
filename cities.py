import json
from nanoid import generate

states_codes = {}
cities = []

with open('json/estados.json', encoding='utf-8-sig') as states_file:
  states = json.load(states_file)

  for state in states:
    states_codes[state['codigo_uf']] = {
      'state_letter': state['uf'],
      'state': state['nome']
    }

with open('json/municipios.json', encoding='utf-8-sig') as cities_file:
  cities_json = json.load(cities_file)

  for city in cities_json:
    cities.append({
      'id': generate(size=8),
      'name': city['nome'],
      'state_letter': states_codes[city['codigo_uf']]['state_letter'],
      'state': states_codes[city['codigo_uf']]['state'],
      '_geo': {
        'lat': city['latitude'],
        'lng': city['longitude'],
      }
    })

if (cities):
  with open('cities.json', 'w', encoding='utf-8') as outfile:
    json.dump(cities, outfile)