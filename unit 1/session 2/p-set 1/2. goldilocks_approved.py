"""
Problem: Return any number from a list of distinct positive integers that is neither the min nor max value in the array. If there is no such number return -1

Understand: 

input = list(int) 0 < int < +inf
ouput = int (not min or max, if none, -1)

Plan(s):

Min Max, Time, Space
"""

class goldilocksApproved:
    def __init__(self, nums):
        self.nums = nums

    def minMax(self):
        if len(self.nums) < 3:
            return -1
        for num in self.nums:
            if num != min(self.nums) and num != max(self.nums):
                return num
        return -1



if __name__ == "__main__":
    def run_tests(test_list):
        for test in test_list:
            # number of var (one, two, etc) == number of methods for problem
            one = goldilocksApproved(test)
            print(f"Test: {test}")
            print(f"MinMax: {one.minMax()}")
            print()

    test_list = [
        [3, 2, 1, 4],
        [1, 2],
        [2, 1, 3],
    ]

    run_tests(test_list)