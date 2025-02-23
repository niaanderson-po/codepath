"""
Problem: Take a list of strings words and a string s, and return True if s is an acronym of words, otherwise return False

Understand:

input = list(str)
ouput = bool

Plan(s):

Slice, Time, Space
# initialize acronoym
# check if lengths are different
# loop through words
# of each word add the first chara in word to acryonmy
# return arconym
"""

class isAcronym:
    def __init__(self, words, target):
        self.words = words
        self.target = target

    def slice(self):
        if len(self.target) != len(self.words):
            return False

        acronym = ""
        for word in self.words:
            acronym += word[0]
        return acronym == self.target


if __name__ == "__main__":
    def run_tests(test_list):
        for test in test_list: 
            # number of var (one, two, etc) == number of methods for problem
            one = isAcronym(test[0], test[1])
            print(f"Test: {test}")
            print(f"Slice: {one.slice()}")
            print()

    test_list = [
        [["christopher", "robin", "milne"], "crm"],
        [["pooh", "bear"], "pb"]
    ]

    run_tests(test_list)