def moveZeros(nums):
    j = 0
    for i in range(len(nums)):
        if i < len(nums) and nums[i] == 0:
            continue
        else:
            nums[j] = nums[i]
            j += 1
    nums[j:] = [0] * len(nums[j:])