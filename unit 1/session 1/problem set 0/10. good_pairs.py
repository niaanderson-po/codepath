"""
Problem: Take two integer arrays pile1 and pile2, and a positive integer k, returning the number of good pairs. A pair (i, j) is good if pile1[i] is divisible by pile2[j] * k.

Understand:

input = 2 lst(int), int
ouput = str

Decision - pile1[i] % (piles2[j] * k) = 0

Plan(s):

Nested Loop, Time, Space
# i
# j
# for i in pile1
# for j in pile2
# if pile1[i] % (piles2[j] * k) == 0
# increment goodPairCount by 1
"""

class goodPairs:
    def __init__(self, pile1, pile2, k):
        self.pile1 = pile1
        self.pile2 = pile2
        self.k = k

    def nestedLoop(self):
        goodPairCount = 0
        for i in range(len(self.pile1)):
            for j in range(len(self.pile2)):
                if self.pile1[i] % (self.pile2[j] * self.k) == 0:
                    goodPairCount += 1
        return goodPairCount

if __name__ == "__main__":
    def run_tests(test_list):
        for test in test_list:
            one = goodPairs(test[0], test[1], test[-1])
            print(f"Test: {test}")
            print(f"Nested Loop: {one.nestedLoop()}")
            print()

    test_list = [
        [[1, 3, 4], [1, 3, 4], 1],
        [[1, 2, 4, 12], [2, 4], 3],
        [[2, 4, 6], [1, 1, 1], 2],
        [[], [1, 2, 3], 1]
    ]

    run_tests(test_list)

