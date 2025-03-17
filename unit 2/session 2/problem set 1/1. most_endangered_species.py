"""
input: lst[dic]
output: str

plan:

"""
def most_endangered(species_list):
    min_pop = float('inf')
    min_name = ""
    for species in species_list:
        if species["population"] < min_pop:
            min_pop = species["population"]
            min_name = species["name"]
    
    return min_name

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 10
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))