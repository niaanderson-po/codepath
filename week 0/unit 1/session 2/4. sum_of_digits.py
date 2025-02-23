"""
Problem: Take a list of integers and continuously remove the minimum element until the list is empty. Return a new list of the removed elements in order.

Understand:

input = int
ouput = int (after algorithmic expression)

Plan(s):

While Loop, Time, Space
# initialize sum
# while num > 0:
# add last digit (num%10) to sum
# remove last digit (num//=10)
# return sum
"""

class sumOfDigits:
    def __init__(self, num):
        self.num = num

    def whileLoop(self):
        sum = 0
        num = self.num
        while num > 0:
            sum += num%10
            num //= 10
        return sum

if __name__ == "__main__":
    def run_tests(test_list):
        for test in test_list: 
            # number of var (one, two, etc) == number of methods for problem
            one = sumOfDigits(test)
            print(f"Test: {test}")
            print(f"While Loop: {one.whileLoop()}")
            print()

    test_list = [
        423,
        23,
        3,
        1001,
    ]

    run_tests(test_list)
