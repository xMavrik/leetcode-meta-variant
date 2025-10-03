
"""
merge 3 sorted lists of integers into 1 sorted list.
remove duplicates.

a = [1,2,4]
b = [2,3]
c = [2,5]
output = [1,2,3,4,5]

"""

# just adding some more testing here


def merge_three_sorted_lists_unique(a, b, c):
    i = j = k = 0
    merged = []
    prev = None   # track last appended value

    candidates = []
    
    while i < len(a) or j < len(b) or k < len(c):
        # pick the smallest candidate among a[i], b[j], c[k]
        if i < len(a):
            candidates.append([a[i], 'a'])
        if j < len(b):
            candidates.append([b[j], 'b'])
        if k < len(c):
            candidates.append([c[k], 'c'])
        
        val, src = min(candidates)
        
        # only append if not a duplicate of the last value
        if prev != val:
            merged.append(val)
            prev = val
        
        if src == 'a': 
            i += 1
        elif src == 'b': 
            j += 1
        else: 
            k += 1

        candidates = []

    return merged


#a = [1,2,4]
#b = [2,3]
#c = [2,5]

#print(merge_three_sorted_lists_unique(a, b, c))


#testing

"""
merge k lists

a = [1,2,4]
b = [2,3]
c = [2,5]
output = [1,2,3,4,5]

"""

import heapq


def mergeKLists(lists):
    # Min-heap
    min_heap = []
    
    # Initialize heap with the first element of each list
    for i, list in enumerate(lists):
        if list:
            heapq.heappush(min_heap, (list[0], i, 0))


    result = []

    print(min_heap)
    
    # Process heap
    while min_heap:
        val, list_index, index = heapq.heappop(min_heap)

        result.append(val)
        
        # Move to the next element in the same list
        index += 1
        if index < len(lists[list_index]):
            heapq.heappush(min_heap, (lists[list_index][index], list_index, index))
    
    return result


a = [1,2,4]
b = [2,3]
c = [2,5]

print(mergeKLists([[1,2,4], [2,3], [-1,5]]))
