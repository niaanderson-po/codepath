"""
Problem: Take an integer array nums and return the minimum number of operations required to make all elements divisible by 3. Each operation consists of adding or subtracting 1 from any element.

Understand:

input = lst(int)
ouput = int (min num of operations -add or subtract- for each ele%3=0)

Plan(s):

For Loop, Time, Space
# loop through nums
# check if num divisible by 3 by remainder
# if remainder 1 increment operation 1 one subtract 1
# if remainder is 2 increment operations by 1 add 1
# means:
    # 1 → num is 1 more than a multiple of 3 (e.g., 4, 7, 10)
    # 2 → num is 2 more than a multiple of 3 (e.g., 5, 8, 11)
# return operation total
"""

class finalValueAfterOperations:
    def __init__(self, nums):
        self.nums = nums

    def forLoop(self):
        operations = 0
        for num in self.nums:
            remainder = num % 3
            if remainder == 1:
                operations += 1 
            elif remainder == 2:
                operations += 1 
        return operations

if __name__ == "__main__":
    def run_tests(test_list):
        for test in test_list: 
            # number of var (one, two, etc) == number of methods for problem
            one = finalValueAfterOperations(test)
            print(f"Test: {test}")
            print(f"For Loop: {one.forLoop()}")
            print()

    test_list = [
        [1, 2, 3, 4],
        [3, 6, 9]
    ]

    run_tests(test_list)

