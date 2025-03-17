"""
input lst[dic]
output lst[str]

iterate through nft_collection
each i extract name value 
append to a lst
return lst
"""

def extract_nft_names(nft_collection):
    result = []
    for ele in nft_collection:
        result.append(ele["name"])
    
    return result

"""
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))
"""

def identify_popular_creators(nft_collection):
    from collections import Counter
    creator = []
    
    for ele in nft_collection:
        creator.append(ele["creator"])

    fmap = Counter(creator)

    result = []
    for creator in fmap:
        if fmap[creator] > 1:
            result.append(creator)
    
    return result

"""

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
"""

def average_nft_value(nft_collection):
    if len(nft_collection) == 0:
        return 0
    
    total_value = 0
    for nft in nft_collection:
        total_value += nft["value"]

    return total_value/len(nft_collection)

"""

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))
"""

def search_nft_by_tag(nft_collections, tag):
    result = []

    for collection in nft_collections:
        for nft in collection:
            if tag in nft["tags"]:
                result.append(nft["name"])

    return result

"""

nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))
"""

def process_nft_queue(nft_queue):
    result = []
    for ele in nft_queue:
        result.append(ele["name"])
    
    return result

"""

nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3))
"""

"""
input lst[str]
output bool

iterate actions
count += 1 if "add"
count -= 1 if "remove"
if count < 0 return false

if count != 0 return false
return true

"""
def validate_nft_actions(actions):

    # count = 0

    # for action in actions:
    #     if action == "add":
    #         count += 1
    #     else:
    #         count -= 1
        
    #     if count < 0:
    #         return False

        
    # if count != 0:
    #     return False
    
    # return True if count == 0 else False

        #or

    stack = []

    for action in actions:
        if action == "add":
            stack.append(action)
        elif action == "remove":
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

"""

actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))

"""

"""
input lst[float]
output tuple(float)

iterate
below
above
if current <= target
below = max(below, current)
if current >= target
above = min(above, current)
"""
def find_closest_nft_values(nft_values, budget):
    below = float('-inf')
    above = float('inf')

    for nft_value in nft_values:
        if nft_value <= budget:
            below = max(below, nft_value)
        elif nft_value >= budget:
            above = min(above, nft_value)

    return (below,above)

#alternative approach: binary search

nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))
