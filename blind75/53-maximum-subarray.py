def maxSubArray(nums):
    """
    Find the contiguous subarray with the largest sum (Kadane's Algorithm).
    Uses O(n) time and O(1) space.
    
    Key insight: At each position, we decide:
    - Should we EXTEND the previous subarray (add current to currSum)?
    - Or START FRESH from current element?
    
    Answer: If currSum < 0, starting fresh is always better!
    Because adding anything to a negative sum makes it smaller.
    """
    
    # Track the maximum sum found so far
    # Initialize with first element to handle all-negative arrays
    maxSum = nums[0]
    
    # Track the current subarray sum
    currSum = 0

    for num in nums:
        # Key decision: Should we include previous elements?
        # If currSum is negative, it would only drag down our sum
        # So we reset and start fresh from current number
        if currSum < 0:
            currSum = 0
        
        # Add current number to our running sum
        currSum = currSum + num
        
        # Update maximum if current sum is better
        maxSum = max(maxSum, currSum)
        
    return maxSum

"""
Kadane's Algorithm Intuition:

For each element, we ask:
"Is it better to extend the previous subarray or start a new one here?"

If previous sum (currSum) is negative → start fresh (currSum = 0)
If previous sum is positive → extend it (adds value)

Example walkthrough with nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]:

  num=-2: currSum<0? No(0), currSum=0+(-2)=-2, maxSum=max(-2,-2)=-2
  num=1:  currSum<0? Yes(-2), reset to 0, currSum=0+1=1, maxSum=max(-2,1)=1
  num=-3: currSum<0? No(1), currSum=1+(-3)=-2, maxSum=max(1,-2)=1
  num=4:  currSum<0? Yes(-2), reset to 0, currSum=0+4=4, maxSum=max(1,4)=4
  num=-1: currSum<0? No(4), currSum=4+(-1)=3, maxSum=max(4,3)=4
  num=2:  currSum<0? No(3), currSum=3+2=5, maxSum=max(4,5)=5
  num=1:  currSum<0? No(5), currSum=5+1=6, maxSum=max(5,6)=6 ← BEST!
  num=-5: currSum<0? No(6), currSum=6+(-5)=1, maxSum=max(6,1)=6
  num=4:  currSum<0? No(1), currSum=1+4=5, maxSum=max(6,5)=6

Answer: 6 (subarray [4,-1,2,1])

Time Complexity: O(n) - single pass
Space Complexity: O(1) - only tracking two variables
"""

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))