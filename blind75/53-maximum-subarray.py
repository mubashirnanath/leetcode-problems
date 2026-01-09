def maxSubArray(nums):
    maxSum = nums[0]
    currSum = 0

    for num in nums:
        if currSum<0:   # if currSum become -ve then make it 0, because we dont get higher number when we add anything with -ve number
            currSum = 0
        currSum = currSum+num        # add current number to currSum
        maxSum = max(maxSum, currSum) # check which is largest
    return maxSum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))