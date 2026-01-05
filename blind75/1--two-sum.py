def twoSum(nums, target):
    prev_map = dict()

    for i, num in enumerate(nums):
        if target - num in prev_map:
            return  [i, prev_map[target-num]]
        prev_map[num] = i

    return -1
        
arr = [2, 7, 11, 15]
target = 9
print(twoSum(arr, target))