"""

1539. Kth Missing From the Left


Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth missing number starting from leftmost number of array

Here we are not assuming array starts at 1, it starts at the first num of input array


ASKING FOR FIRST DAY A PROJECT CAN BE COMPLETED
META WILL REPHRASE THIS PROBLEM TO BE A LIST OF HOLIDAYS THAT YOU CANNOT WORK, AND K IS THE NUMBER OF DAYS REQUIRED TO COMPLETE THE PROJECT


Example 1:

Input: arr = [4, 7, 9, 10], k = 1
Output: 5
Explanation: First missing number is 5


Input: arr = [4, 7, 9, 10], k = 3
Output: 8
Explanation: Missing numbers are [5, 6, 8], therefore its 8


Input: arr = [1, 2, 4], k = 3
Output: 6
Explanation: Missing numbers are [3, 5, 6, 7, ...], there for its 6

"""


def getMissingNum(arr, k):

    left = 0

    right = len(arr) - 1


    while left <= right:

        middle = (left + right) // 2

        missing = arr[middle] - 1 - middle

        if missing < k:
            left = middle + 1

        else:
            right = middle - 1


    return arr[0] + k + right

