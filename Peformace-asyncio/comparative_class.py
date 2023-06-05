from pokedex_not_optimized import main_class_not_optmized
from pokedex_optimized import main_optmized
import random

pokemon_list=random.sample(range(1, 100), 12)
time_to_complete_class_optimized = main_optmized(pokemon_list)["time"]
size_of_class_optimized = main_optmized(pokemon_list)["size"]
print(size_of_class_optimized)
time_to_complete_class_not_optimized = main_class_not_optmized(pokemon_list)["time"]
size_of_class_not_optimized = main_class_not_optmized(pokemon_list)["size"]
print(size_of_class_not_optimized)

print(f'Pokedex optimized finished in {time_to_complete_class_optimized:.4} seconds')
print(f'Pokedex NOT optimized finished in {time_to_complete_class_not_optimized:.4} seconds.')
print(f'The Optimized classse performed {(100 - (time_to_complete_class_optimized *100 / time_to_complete_class_not_optimized))} %  faster than the non-optimized class.')