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

    convert word to lowercase so case insensitive
    replace tagets with empty ""
    return
    """
    word = word.lower()
    substrings = {"t", "i", "gg", "er"}

    for sub in substrings:
        word = word.replace(sub, '')
        
    return word

word = "Trigger"
# print(tiggerfy(word))
word = "eggplant"
# print(tiggerfy(word))
word = "Choir"
# print(tiggerfy(word))

#Learned: string method -> .replace(), benefit of set vs lst for stored value extra: research string methods

def non_decreasing(nums):
    """
    input lst[int]
    output bool
    
    initialize count
    iterate through num up to second to last ele
    if 'nums[i] > nums[i+1]', increment count
    if ...
    """
    n = len(nums)
    count = 0

    for i in range(n - 1):
        #violation
        if nums[i] > nums[i+1]:
            count += 1
            #violation allowance
            if count > 1:
                return False
            
            #fixing the violation: 2 options
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                #lower nums[i]
                nums[i] = nums[i + 1]
            else:
                #raise nums[i + 1]
                nums[i + 1] = nums[i]
    return True

nums = [4, 2, 3]
# print(non_decreasing(nums))

nums = [3, 4, 2, 3]
# print(non_decreasing(nums))

nums = [5, 7, 1, 8]
# print(non_decreasing(nums))

#Learned: in bound/out of bound prevention, walk through example logic slowly and carefully to develop solution intuition ie what data is important to identify, what specifically needs to change, how to conduct change, based on what requirments/checks, why, etc

#Problem 5
def find_missing_clues(clues, lower, upper):
   """
   3 input int int lst[int]
   output lst[int](sorted)
   """
   missing_ranges = []
   clues.sort()
   
   # Check the gap between lower and the first clue
   if lower < clues[0]:
       missing_ranges.append([lower, clues[0] - 1])
    
   # Check gaps between consecutive clues
   for i in range(1, len(clues)):
    if clues[i - 1] + 1 < clues[i]:
        missing_ranges.append([clues[i - 1] + 1, clues[i] - 1])
    
   # Check the gap between the last clue and upper
   if clues[-1] < upper:
    missing_ranges.append([clues[-1] + 1, upper])
    
   return missing_ranges 

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
# print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
# print(find_missing_clues(clues, lower, upper))

#Learned: an example of when to use .sort() a string method, test difference btw sort & sorted, when to recall .append(), how to set indexes within a lst, nested lst, benefits of drawing output templat/structure

#Problem 6
def harvest(vegetable_patch):
    """
    input 2d matrix
    output int rep 'c'
    """
    # Initialize the carrot counter
    carrot_count = 0
    
    # Get the number of rows (n) and columns (m)
    n = len(vegetable_patch)
    m = len(vegetable_patch[0])
    
    # Traverse the 2D matrix
    for row in range(n):
        for col in range(m):
            # Check if the current element is 'c'
            if vegetable_patch[row][col] == 'c':
                # Increment the carrot counter
                carrot_count += 1
    
    # Return the total number of carrots
    return carrot_count

#Learned: how to get the # of rows & col + traverse for target (nested loops)

#Problem 7
def good_pairs(pile1, pile2, k):
    """
    3 input: lst[int] lst[int] int
    ouput: int
    """
    pass