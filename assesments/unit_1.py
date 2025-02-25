#Unique
def unique(s):
    map = {}
    for char in s:
        if char in map:
            return False
        else:
            map[char] = 1
    return True

#Needle in Haystack
def needle_in_haystack(needle, haystack):
    pointer = 0
    
    for i in range(len(haystack)):
        if haystack[i] == needle[pointer]:
            indexOfCurrent = i + 1
            pointer += 1
        else:
            pointer = 0
            
        if pointer == len(needle):
            return indexOfCurrent-len(needle)
    return -1

#flowerbed [0,1,0,0,1]
def flowerbed(bed, n):
    for spot in range(len(flowerbed)):
        if flowerbed[spot] == 0:
            if spot == 0:
                if flowerbed[spot+1] == 0:
                    flowerbed[spot] = 1
                    n -= 1
            if spot != 0 and spot != len(flowerbed)-1:
                if flowerbed[spot-1] == 0 and flowerbed[spot+1] == 0:
                    flowerbed[spot] = 1
                    n -= 1
            if spot == len(flowerbed) - 1:
                if flowerbed[spot-1] == 0:
                    flowerbed[spot] = 1
                    n-= 1
        if n == 0:
            return True
    if len(flowerbed) == 0 and n == 0:
        return True
    return False

#Output of Snippet
name = "codepath"
name[0] = "C"

#Answer: D - Throws an error because strings are immutable and characters cannot be changed once the string is created.

def mystery_function(s):
    count = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
    return count

result = mystery_function("AABBAB")
print(result)

#Answer 2

def mystery_function(lst, threshold):
    total = 0
    i = 0

    while i < len(lst) and total + lst[i] <= threshold:
        total += lst[i]
        i += 1
    return total

result = mystery_function([1,2,3,4,5,6], 7)
print(result)

#Answer 6

#Find the bug
#Old code:
def reverse_lst(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1 
    
    return lst

#New code:
def reverse_lst(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1 
    
    return lst

#Answer No temp variable for swap and left/right incrementing/decrementing wrong