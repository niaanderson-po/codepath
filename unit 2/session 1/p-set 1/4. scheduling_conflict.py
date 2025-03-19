"""
plan:
loop through each key:value in venue1_schedule
if that key:value is in venue2_schedule
add to output map
return output map
"""

def identify_conflicts(venue1_schedule, venue2_schedule):
    output = {}
    for key, values in venue1_schedule.items():
        if values == venue2_schedule.get(key):
            output[key] = values
    return output

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))    

