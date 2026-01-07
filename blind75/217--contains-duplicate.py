def containsDuplicate(nums):
    prev_map = dict()

    for i, num in enumerate(nums):
        if num in prev_map:
            return False
        else:
            prev_map[num] = i
    return True

nums = [1,2,3,4]
print(containsDuplicate(nums))