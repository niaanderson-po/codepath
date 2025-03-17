#technical question: what if the artist have multiple times
        
def lineup(artists, set_times):
    output = {}
    for i in range(len(artists)):
        output[artists[i]] = set_times[i]
    return output

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia", "Kendrick Lamar"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM","6:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))