"""

Given an array of pairs dominoes and an integer target, return the number of unique domino pairs [a1,a2] and [b1,b2] where a1 + b1 = target and a2 + b2 = target.

Note: Numbers are limited to digits 0-9. Additionally, you may not use the same pair with itself.

Example 1:
Input: nums = [[3,4],[1,9],[3,4],[2,1],[9,1],[9,1],[7,6],[1,9]], target = 10
Output: 6

Example 2:
Input: nums = [[0,0],[0,0],[0,0],[0,0],[0,0]], target = 10
Output: 10


[3, 4] --> [7, 6] is a match 
3 + 7 = 10
4 + 6 = 10


"""
import collections

def twoSum(nums, target):

    targ = collections.defaultdict(int)

    counter = 0

    for x, y in nums:

        targetx = target - x
        targety = target - y

        newTarget = targetx * 10 + targety

        if newTarget in targ:
            counter += targ[newTarget]

        aTarget = x * 10 + y

        targ[aTarget] += 1

    return counter

nums = [[3,4],[1,9],[3,4],[2,1],[9,1],[9,1],[7,6],[1,9]]
target = 10

print(twoSum(nums, target))