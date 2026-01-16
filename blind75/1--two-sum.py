def twoSum(nums, target):
    """
    Find two numbers in the array that add up to target.
    Returns their indices. Uses HashMap for O(n) time complexity.
    """
    
    # HashMap to store: number -> its index
    # This allows O(1) lookup to check if complement exists
    prev_map = dict()

    for i, num in enumerate(nums):
        # Calculate the complement needed to reach target
        # If current num + complement = target, then complement = target - num
        complement = target - num
        
        # Check if we've seen the complement before
        if complement in prev_map:
            # Found it! Return both indices
            # prev_map[complement] is the index of the complement
            # i is the index of current number
            return [i, prev_map[complement]]
        
        # Haven't found a pair yet, store current number and its index
        # for future lookups
        prev_map[num] = i

    # No solution found (problem guarantees one exists)
    return -1

"""
Why HashMap works:
- For each number, we need to find if (target - num) exists in array
- Instead of O(n) search each time, store seen numbers in HashMap
- Lookup in HashMap is O(1), making total time O(n)

Example walkthrough with nums=[2,7,11,15], target=9:
  i=0: num=2, need 9-2=7, not in map, store {2:0}
  i=1: num=7, need 9-7=2, found 2 at index 0! Return [1,0]
"""
        
arr = [2, 7, 11, 15]
target = 9
print(twoSum(arr, target))