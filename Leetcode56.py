"""

Given two array intervals A and B where intervals in A have no overlap in A and intervals in B have no overlap in B. 

Furthermore, A[i], B[i] = [startᵢ, endᵢ], merge all overlapping intervals between the two interval lists, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Note: Both A and B are sorted by start in ascending order.

Example 1:

Input:
A = [[3,11], [14,15], [18,22], [23,24], [25,26]]
B = [[2,8], [13,20]]

Output: [[2,11], [13,22], [23,24], [25,26]]

Example 2:

Input:
A = []
B = [[0,4], [10,13]]

Output: [[0,4], [10,13]]

"""

#[3, 11], [14, 15]
#[2, 8], [9, 15]


#[2, 11] -> [9, 15] = [2, 15]

#[1, 5]
#[6, 8]


def mergeIntervals(A, B):

    left = 0

    right = 0

    response = []

    def add_interval(start, end):
        if not response or response[-1][1] < start:
            response.append([start, end])
        else:
            response[-1][1] = max(response[-1][1], end)


    while left < len(A) and right < len(B):

        left_beg, left_end = A[left]
        right_beg, right_end = B[right]

        if left_beg <= right_beg:
            add_interval(left_beg, left_end)
            left += 1
        else:
            add_interval(right_beg, right_end)
            right += 1

    # if we break and either point is still less, add the whole thing, iteratively

    while left < len(A):
        add_interval(A[left][0], A[left][1])
        left += 1

    while right < len(B):
        add_interval(B[right][0], B[right][1])
        right += 1

    return response


A = [[3,11], [14,15], [18,22], [23,24], [25,26]]
B = [[2,8], [13,20]]

A1 = []
B1 = [[0,4], [10,13]]


print(mergeIntervals(A, B))