def containsDuplicates(nums):
    if len(set(nums)) < len(nums):
        return True
    return False
