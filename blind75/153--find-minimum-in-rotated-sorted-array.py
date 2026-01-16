def findMin(nums):
    """
    Find the minimum element in a rotated sorted array.
    Uses modified binary search for O(log n) time.
    
    Key insight: In a rotated sorted array, one half is always sorted.
    The minimum is at the "rotation point" where the order breaks.
    
    Example: [4,5,6,7,0,1,2] - rotated at index 4, minimum is 0
    """

    # Initialize result with first element
    res = nums[0]
    
    # Binary search pointers
    l = 0
    r = len(nums) - 1

    while l <= r:
        # If current subarray is already sorted (no rotation in this part)
        # The minimum is at the left end
        if nums[l] <= nums[r]:
            res = min(res, nums[l])
            break  # Found minimum, no need to continue

        # Calculate middle index
        mid = (l + r) // 2
        
        # Update result with mid value (could be the minimum)
        res = min(res, nums[mid])

        # Decide which half to search
        # If left half is sorted (nums[l] <= nums[mid])
        # then minimum must be in the RIGHT half (unsorted part)
        if nums[l] <= nums[mid]:
            # Left side is sorted, minimum is in right side
            # Example: [4,5,6,7,0,1,2], mid=7, go right to find 0
            l = mid + 1
        else:
            # Right side is sorted, minimum is in left side
            # Example: [6,7,0,1,2,4,5], mid=1, go left to find 0
            r = mid - 1
        
    return res

"""
Binary Search Logic for Rotated Array:

Original sorted: [0,1,2,4,5,6,7]
Rotated:         [4,5,6,7,0,1,2]  (rotated 4 times)
                      ↑
                  rotation point (minimum)

Key observations:
1. If nums[l] <= nums[r] → subarray is sorted, minimum at left
2. If nums[l] <= nums[mid] → left half sorted, minimum in right half
3. Otherwise → right half sorted, minimum in left half

The minimum is always in the UNSORTED half!

Time Complexity: O(log n) - binary search
Space Complexity: O(1)
"""

nums = [4,5,6,7,0,1,2]
print(findMin(nums))