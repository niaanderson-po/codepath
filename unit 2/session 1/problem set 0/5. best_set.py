"""
plan:
initalize a dict
loop through votes
if value is not a key in new dict, add
if it is increment by 1
return max(dict)

plan:
count occurrences of each canidate aka the values 
return max(dict)

plan:
"""

def best_set(votes):
    result = {}
    for key in votes:
        if votes[key] not in result:
            result[votes[key]] = 1
        else:
            result[votes[key]] += 1
    return max(result, key=result.get)

    #or

    from collections import Counter
    result = Counter(votes.values())
    return max(result, key=result.get)

    #or

    from collections import defaultdict
    result = defaultdict(int)
    for value in votes.values():
        result[value] += 1
    return max(result, key=result.get)


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))