def missingNumber(nums):
    n = len(nums)
    for i in range(n+1):
        if i not in nums:
            return i
