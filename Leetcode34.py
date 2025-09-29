nums = [5, 5, 5, 5, 8, 8, 8, 9, 9, 9, 9, 9, 9]


# count the amount of unique chars

def getUnique(nums):

    def getBounds(nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return right


    count = 0
    i = 0

    while i < len(nums):

        count += 1

        i = getBounds(nums, nums[i] + 1)

    return count


