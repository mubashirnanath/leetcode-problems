def maxProduct(nums):
    """
    Find the contiguous subarray with the largest product.
    Uses dynamic programming tracking both min and max products.
    
    Key insight: A negative number can turn a minimum product into maximum
    (and vice versa), so we need to track BOTH min and max at each step.
    """

    # Initialize result with first element (handles single element case)
    res = nums[0]
    
    # Track current minimum and maximum products ending at current position
    # Start with 1 (neutral for multiplication) - will be updated on first iteration
    currMin, currMax = 1, 1

    for num in nums:
        # Store currMax because we'll update it before using in currMin calculation
        temp = currMax
        
        # Calculate new maximum product ending here
        # Three choices:
        # 1. currMax * num: extend the previous max subarray
        # 2. currMin * num: if num is negative, min becomes max!
        # 3. num: start fresh from current number
        currMax = max(temp * num, currMin * num, num)
        
        # Calculate new minimum product ending here
        # Same logic - we need min because it could become max later
        currMin = min(temp * num, currMin * num, num)

        # Update global result
        res = max(res, currMax)
        
    return res

"""
Why track both min AND max?

Consider [-2, 3, -4]:
  num=-2: currMax=-2, currMin=-2, res=-2
  num=3:  currMax=3, currMin=-6, res=3
  num=-4: currMax=(-6)*(-4)=24! currMin=-12, res=24

The -6 (minimum) became 24 (maximum) when multiplied by -4!
This is why we can't just track maximum - negatives flip everything.

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only tracking a few variables
"""

nums = [2, 3, -2, 4]
print(maxProduct(nums))