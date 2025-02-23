"""
Problem: Take an integer num and return the sum of its digits.

Understand:

input = list(str)
ouput = int -> tigger/value after operations

Plan(s):

If Else, Time, Space
# loop through operations
# if ele match increment operations, increment
# else decrement
# return tigger

Hash Map, Time, Space
# initaialize a map with operation:value
# loop through operations
# if current match key, update tigger to reflect value
# return tigger
"""

class finalValueAfterOperations:
    def __init__(self, operations):
        self.operations = operations
        self.tigger = 1

    def ifElse(self):
        for operation in self.operations:
            if operation == "bouncy" or operation == "flouncy":
                self.tigger += 1
            elif operation == "trouncy" or operation == "pouncy":
                self.tigger -= 1
        return self.tigger

    def hashMap(self):
        mapping = {
            "bouncy": 1,
            "flouncy": 1,
            "trouncy": -1,
            "pouncy": -1,
        }

        for operation in self.operations:
            self.tigger += mapping[operation]
        return self.tigger

if __name__ == "__main__":
    def run_tests(operations_list):
        for test in test_list:
            one = finalValueAfterOperations(test)
            two = finalValueAfterOperations(test)
            print(f"Test: {test}")
            print(f"If Else: {one.ifElse()}")
            print(f"Hash Map: {two.hashMap()}")
            print()

    test_list = [
        ["trouncy", "flouncy", "flouncy"],
        ["bouncy", "bouncy", "flouncy"],
        ["trouncy", "flouncy", "flouncy", "bouncy"],
    ]

    run_tests(test_list)