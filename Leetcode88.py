"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order. FOR THE VARIANT WE ARE NOT GIVEN THE SIZE M OR SIZE N

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.

Example 1:

Input: nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1],  nums2 = [],
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], nums2 = [1]
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

"""


from typing import List


def merge(nums1: List[int], nums2: List[int]) -> None:

    # we know nums1 is double the size of nums2
    # just make custom var for m and n

    m_idx = int(len(nums1) / 2) - 1

    n_idx = len(nums2) - 1

    last = len(nums1) - 1

    while n_idx >= 0:

        if nums1[m_idx] > nums2[n_idx] and m_idx >= 0:
            nums1[last] = nums1[m_idx]
            m_idx -= 1

        else:
            nums1[last] = nums2[n_idx]
            n_idx -= 1

        last -= 1


#-------- Test Cases -----------------
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge(nums1, nums2)
print(nums1)
