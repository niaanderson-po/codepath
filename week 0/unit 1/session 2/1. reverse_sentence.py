"""
Problem: Reverse a string. If there is only one word in the sentence, the function should return the original string.

Understand: 

input = str
ouput = str

Plan(s):

Slice, O(n), O(n)
# split sentence using split()
# reverse list using slicing
# join the revered list using join()
# return str
"""

class reverseSentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def slice(self):
        sentence = self.sentence.split()
        return " ".join(sentence[::-1])



if __name__ == "__main__":
    def run_tests(test_list):
        for test in test_list:
            one = reverseSentence(test)
            print(f"Test: {test}")
            print(f"Slice: {one.slice()}")
            print()

    test_list = [
        "tubby little cubby all stuffed with fluff",
        "Pooh",
    ]

    run_tests(test_list)

