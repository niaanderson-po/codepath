def linear_search(lst, target):
    """
    2 inputs: lst str
    output: int -> index or -1

    iterate through lst 
    if current ele is target
    return index
    if no index returned, return -1 outside of loop

    o(n)
    o(1) not using any additonal memory 
    """

    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
# print(linear_search(items, target))
items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
# print(linear_search(items, target))

def final_value_after_operations(operations):
    """
    either create a dict for efficent accesseing + readability + scalability/modification (extra memeory) or simply use conditionals
    
    *ask should I priroritze time or space complexity?
    *ask would operations included any other operations

    iterate through operations
    check if currrent is flouncy and bouncy if yes increment 1
    else decrement 1
    """
    count = 1
    for ele in operations:
        if ele == "bouncy" or ele == "flouncy":
            count += 1
        else:
            count -= 1
    return count

operations = ["trouncy", "flouncy", "flouncy"]
# print(final_value_after_operations(operations))
operations = ["bouncy", "bouncy", "flouncy"]
# print(final_value_after_operations(operations))

def tiggerfy(word):
    """
    input str
    output str

    *ask can i use a built in function like find

    convert word to lowercase so case insensitive
    create list of substring
    iterate through string
    if current in substring
    continue
    else add current to new string
    return new string
    """
    word = word.lower()
    substrings = ["t", "i", "gg", "er"]
    substrings2 = ["gg", "er"]
    new_word = ""

    for current in substrings:
        idx = word.find(current)
        print(idx)
        

    return new_word

word = "Trigger"
print(tiggerfy(word))
word = "eggplant"
print(tiggerfy(word))
word = "Choir"
print(tiggerfy(word))

#ERROR is this current logic doesnt account for substriong with various lengths

def non_decreasing(nums):
    """
    input lst[int]
    output bool
    
    """