
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



def findBuildings(heights) -> List[int]:

    stack_left = []

    max_left = 0

    stack_right = []

    max_right = 0

    left, right = 0, len(heights) - 1

    while left <= right:

        if heights[left] > max_left:
            max_left = heights[left]
            stack_left.append(left)

        left += 1

        if heights[right] > max_right:
            max_right = heights[right]
            stack_right.append(right)

        right -= 1

    stack_left.extend(stack_right[::-1])

    return stack_left


heights1 = [2, 5, 3, 10, 9, 8]

print(findBuildings(heights1))

def test_answer():
    assert findBuildings(heights1) == [0, 1, 3, 4, 5]