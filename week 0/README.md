# Strings and Arrays

Performing advanced string manipulation and analysis by accessing, iterating, and modifying lists.

Note: _Developing the skill of using the UPI method on every coding problem._

# File Template

```python

"""
Problem: One sentence summary

Understand:

input =
ouput =

Plan(s):

Method, Time, Space
#step by step
"""

class problemName:
    def __init__(self, paramater):
        self.paramater = paramater
        
    def methodName(self):
        pass

if __name__ == "__main__":
    def run_tests(test_list):
        for test in test_list:
            # number of var (one, two, etc) == number of methods for problem
            one = problemName(test)
            print(f"Test: {test}")
            print(f"methodName: {one.methodName()}")
            print()

    test_list = [
        "test string 1",
        "test string 2",
    ]

    run_tests(test_list)
```
