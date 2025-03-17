def navigate_research_station(station_layout, observations):
    layout_index = {}
    for i, ele in enumerate(station_layout):
        layout_index[ele] = i
    
    current = 0
    result = 0
    
    for ele in observations:
        target = layout_index[ele]
        result += abs(current - target)
        current = target
    return result

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))