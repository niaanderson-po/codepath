"""
Problem: Take two integer lists lst1 and lst2 and return a new list that contains elements that are exclusive to each list (i.e., elements that are in lst1 but not in lst2, and vice versa).

Understand:

input = 2 lst(str)
ouput = lst(str)

Does the arrangements of the elements in the new list matter? For example does lst1's elements have to come before lst2's? 

Plan(s):

For Loop, O(n*m), Space
# for word in lst1:
# if word not in lst2:
# append to exclude list 1
# for word in lst2:
# if word not in lst1:
# append to exclude list 2
# return exclude list 1 + exclude list 2

Hash Map,  O(n+m), Space

Symmetric Operator, O(n+m), Space
# return list of set lst1, set lst2 using symmetric operator (^)
"""

class exclusiveElemts:
    def __init__(self, lst1, lst2):
        self.lst1 = lst1
        self.lst2 = lst2

    def forLoops(self):
        exclusive_lst1 = []
        exclusive_lst2 = []
        for word in self.lst1:
            if word not in self.lst2:
                exclusive_lst1.append(word) 
        for word in self.lst2:
            if word not in self.lst1:
                exclusive_lst2.append(word) 
        return exclusive_lst1 + exclusive_lst2

    def hashMap(self):
        from collections import Counter

        freq = Counter(self.lst1) + Counter(self.lst2)
        list = []

        for key, val in freq.items():
            if val == 1:
                list.append(key)
        return list

        # return [key for key, val in freq.items() if val == 1]

    def symmetricOperator(self):
        set1 = set(self.lst1)
        set2 = set(self.lst2)
        return list(set1 ^ set2)

if __name__ == "__main__":
    def run_tests(test_list):
        for test in test_list:
            one = exclusiveElemts(test[0], test[1])
            two = exclusiveElemts(test[0], test[1])
            three = exclusiveElemts(test[0], test[1])
            print(f"Test: {test}")
            print(f"Slice: {one.forLoops()}")
            print(f"Hash Map: {two.hashMap()}")
            print(f"Symmetric Operator: {three.symmetricOperator()}")
            print()

    test_list = [
        [["pooh", "roo", "piglet"], ["piglet", "eeyore", "owl"]],
        [["pooh", "roo"], ["piglet", "eeyore", "owl", "kanga"]],
        [["pooh", "roo", "roo", "piglet"], ["pooh", "roo", "piglet"]]
    ]

    run_tests(test_list)

