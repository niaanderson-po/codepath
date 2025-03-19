"""
input 2 lst[str]: observed (unordered) priority(ordered)
output lst[str] (ordered)

plan:
counter observed o(n)
loop through priority o(n)
for each ele check counter dict
append ele values times
remove ele from observed
extend observed to new list after done iterating through priority
return new list
"""

def prioritize_observations(observed_species, priority_species):
    count = {}
    for ele in observed_species:
        if ele in count:
            count[ele] += 1
        else:
            count[ele] = 1
    result = []

    for ele in priority_species:
        n = count[ele]
        result.extend([ele] * n)
        count[ele] = 0

    for ele in observed_species:
        if count[ele] == 0:
            observed_species.remove(ele)
    
    result.extend(observed_species)
    return result

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 


