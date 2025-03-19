"""
Problem: One sentence Summary

Understand: 

input = unsorted list
output = sorted list

Plan(s):

While Loop, Time, Space
# initialize removed ele list
# while loop to iterate as long as arr exsist
# find min in arr
# append min to new list
# rennove min from arr
# return new list
"""

class deleteMinimumElements:
    def __init__(self, hunny_jar_sizes):
        self.hunny_jar_sizes = hunny_jar_sizes

    def whileLoop(self):
        jars = self.hunny_jar_sizes.copy()
        removedEle = []
        while jars:
            jarMin = min(jars) 
            removedEle.append(jarMin)
            jars.remove(jarMin)
        return removedEle


if __name__ == "__main__":
    def run_tests(test_list):
        for test in test_list:
            # number of var (one, two, etc) == number of methods for problem
            one = deleteMinimumElements(test)
            print(f"Test: {test}")
            print(f"While Loop: {one.whileLoop()}")
            print()

    test_list = [
        [5, 3, 2, 4, 1],
        [5, 2, 1, 8, 2],
        [1, 1, 1, 1],
        [],
    ]

    run_tests(test_list)
            
