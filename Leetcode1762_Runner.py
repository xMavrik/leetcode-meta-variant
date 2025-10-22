
'''
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the left and right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. 
Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [2, 5, 3, 10, 9, 8]
Output: [0, 1, 3, 4, 5]
Explanation: 

'''


from typing import List


class Solution:

    def findBuildings(self, heights):
        pass
        


def test_solution():
    solution = Solution()
    
    # Define test cases
    test_cases = [
        ([2, 5, 3, 10, 9, 8], [0, 1, 3, 4, 5]),
        ([1], [0]),
        ([4, 4, 4, 4], [0, 3]),
        ([10, 9, 8, 7, 6], [0, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]),
        ([3, 4, 3, 2, 1, 5], [0, 1, 5])
    ]

    # Check each test case
    all_passed = True
    for i, (heights, expected) in enumerate(test_cases):
        result = solution.findBuildings(heights)
        if result == expected:
            print(f"Test Case {i + 1}: True")
        else:
            print(f"Test Case {i + 1}: False")
            all_passed = False
    
    return all_passed


# Run the tests
if test_solution():
    print("All test cases passed.")
else:
    print("Some test cases failed.")

