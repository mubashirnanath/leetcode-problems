def containsDuplicate(nums):
    hash_set = set()

    for num in nums:
        if num in hash_set:
            return False
        else:
            hash_set.add(num)
    return True

nums = [1,2,3,1]
print(containsDuplicate(nums))


# simple code
def containsDuplicate(nums):
    return len(nums) == len(set(nums))

nums = [1,2,3,1]
print(containsDuplicate(nums))