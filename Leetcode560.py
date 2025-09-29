"""

560. Subarray Sum Equals K

Medium

Given an array of integers nums and an integer k, return true if there exists a subarray whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: true

Example 2:

Input: nums = [1,4,7], k = 3
Output: false

"""


def sub(nums, k):

    prefix_set = set()

    prefix_sum = 0

    prefix_set.add(0)

    for x in nums:

        prefix_sum += x

        if prefix_sum - k in prefix_set:
            return True
        
        prefix_set.add(prefix_sum)

    return False



nums = [5, -2, 3, -1]
k = 5

nums1 = [1, 4, 7]
k1 = 3

print(sub(nums, k))