def removeDuplicates(nums, val):
    j = 0
    i = 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
            i += 1
    return j

