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


class Solution:
    def mergeSortedArray(self, nums1: list[int], nums2: list[int]):
        a = len(nums1) // 2 - 1
        b = len(nums2) - 1
        i = len(nums1) - 1
        
        while b >= 0:
            if a >= 0 and nums1[a] >= nums2[b]:
                nums1[i] = nums1[a]
                a -= 1
            else:
                nums1[i] = nums2[b]
                b -= 1
            i -= 1

            

if __name__ == "__main__":
    solution = Solution()
    list_a = [1, 3, 0, 0]
    list_b = [4, 10]
    expected = [1, 3, 4, 10]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected

    list_a = [5, 6, 7, 8, 0, 0, 0, 0]
    list_b = [1, 2, 3, 4]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected

    list_a = [0]
    list_b = [99]
    expected = [99]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected

    list_a = [1, 10, 0, 0]
    list_b = [2, 11]
    expected = [1, 2, 10, 11]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected