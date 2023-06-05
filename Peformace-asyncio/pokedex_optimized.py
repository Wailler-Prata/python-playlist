import asyncio
import httpx
from dataclasses import dataclass
import json
import time
import sys
# ============= Setting an inteface to run a GET asyncrono =============
async def get_Async(url, header):
    async with httpx.AsyncClient() as client:
        return await client.get(url=url,headers=header)

async def execute(list_funcs):
    return await asyncio.gather(*list_funcs)

def execute_async(list_funcs):    
    return [ iten.json() for iten in asyncio.run(execute(list_funcs)) ]

# ============= Setting a class for pokemons  =============
@dataclass(repr=False, eq=False, match_args=False, slots=True)
class Pokemon_optimized():
    id_pokemon:int
    name: str
    image: str
    atributes: list[dict]

    def get_pokemon_in_json_format(self):
        return json.dumps({"id_pokemon": self.id_pokemon, "name": self.name.capitalize(), "image": self.image, "atributes": self.atributes}) 

def main_optmized(list_pokemons_id):
    start_time = time.time()
    url = 'https://pokeapi.co/api/v2/pokemon/{}'

    listdata =  execute_async( [get_Async(url.format(id_pokemon), header={}) for id_pokemon in list_pokemons_id] )

    pokemons = [ Pokemon_optimized(id_pokemon=data["id"], name=data["name"], 
                        image = data["sprites"]["front_default"], 
                        atributes=[ {"atribute": json["stat"]["name"], "valor_atribute": json["base_stat"] } 
                        for json in data["stats"] ]
                        ).get_pokemon_in_json_format()
                for data in listdata
                ]
    p = Pokemon_optimized(pokemons[0][0], pokemons[0][1], pokemons[0][2], pokemons[0][3])
    return {"time": time.time() - start_time, "pokemons": pokemons, "size": sys.getsizeof(p)}