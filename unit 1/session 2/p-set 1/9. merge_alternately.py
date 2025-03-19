"""
Problem: Take two strings word1 and word2 and merge them by alternating their letters. If one string is longer, the remaining letters should be appended to the merged string.

Understand:

input = 2 str
ouput = str

Plan(s):

While Loop, Time, Space
"""

class mergeAlternately:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def whileLoop(self):
        i = 0
        j = 0
        string = []
        while i < len(self.word1) and j < len(self.word2):
            string.append(self.word1[i])
            string.append(self.word2[j])
            i += 1
            j += 1
        if i < len(self.word1):
            string.append(self.word1[i:])
        if i < len(self.word2):
            string.append(self.word2[j:])
        return "".join(string)

if __name__ == "__main__":
    def run_tests(test_list):
        for test in test_list:
            one = mergeAlternately(test[0], test[1])
            print(f"Test: {test}")
            print(f"While Loop: {one.whileLoop()}")
            print()

    test_list = [
        ["wol", "oze"],
        ["hfa", "eflump"],
        ["eyre", "eo"]
    ]

    run_tests(test_list)
