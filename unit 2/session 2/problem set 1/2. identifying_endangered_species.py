from collections import Counter
def count_endangered_species(endangered_species, observed_species):
    count = 0
    comparision = set(endangered_species)
    for species in observed_species:
        if species in comparision:
            count += 1
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  
