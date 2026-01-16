def threeSum(nums):
    """
    Find all unique triplets in the array that sum to zero.
    Uses sorting + two-pointer technique for O(n²) time complexity.
    """

    res = []  # Store all valid triplets that sum to 0
    
    # Step 1: Sort the array - this enables the two-pointer technique
    # Example: [-1, 0, 1, 2, -1, -4] becomes [-4, -1, -1, 0, 1, 2]
    nums.sort()

    # Step 2: Fix one number (num) and find two others that sum to -num
    for i, num in enumerate(nums):
        
        # Skip duplicate values for the first number to avoid duplicate triplets
        # If current num equals previous num, we've already found all triplets starting with this value
        if i > 0 and num == nums[i-1]:
            continue
        
        # Step 3: Use two pointers to find pairs that sum to -num
        # Left pointer starts just after current number
        # Right pointer starts at the end of array
        l, r = i+1, len(nums) - 1

        while l<r:
            # Calculate sum of current triplet
            total = num + nums[l] + nums[r]

            if total < 0:
                # Sum is too small, need larger values
                # Move left pointer right to increase the sum
                l = l + 1
            elif total > 0:
                # Sum is too large, need smaller values  
                # Move right pointer left to decrease the sum
                r = r - 1
            else:
                # Found a valid triplet! (total == 0)
                res.append([num, nums[l], nums[r]])
                
                # Move left pointer to find next potential pair
                l = l + 1

                # Skip duplicate values for the second number
                # This avoids adding duplicate triplets to result
                while nums[l] == nums[l-1] and l<r:
                    l = l+1
                    
    return res

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
