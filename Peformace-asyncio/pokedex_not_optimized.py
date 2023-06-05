import requests
import json
import time
from typing import *
import sys

class Pokemon_not_optimized():
    def __init__(self, id_pokemon:int, name:str, image:str, atributes:list[dict]):
        self.id_pokemon=id_pokemon
        self.name=name
        self.image=image
        self.atributes=atributes

    def get_pokemon_in_json_format(self):
        return json.dumps({"id_pokemon": self.id_pokemon, "name": self.name.capitalize(), "image": self.image, "atributes": self.atributes}) 

def main_class_not_optmized(list_pokemons_id):
    start_time = time.time()
    url = 'https://pokeapi.co/api/v2/pokemon/{}'
    pokemons = []
    
    for id_pokemon in list_pokemons_id:
        data = requests.get(url.format(id_pokemon))
        atributes =[]

        for atribute in  data.json()["stats"]:
            atributes.append({"atribute": atribute["stat"]["name"], "valor_atribute": atribute["base_stat"] } )
        
        pokemons.append( Pokemon_not_optimized(id_pokemon=data.json()["id"], name=data.json()["name"], image=data.json()["sprites"]["front_default"], atributes=atributes).get_pokemon_in_json_format())
    p = Pokemon_not_optimized(pokemons[0][0], pokemons[0][1], pokemons[0][2], pokemons[0][3])
    return {"time": time.time() - start_time, "pokemons": pokemons, "size": sys.getsizeof(p)}
