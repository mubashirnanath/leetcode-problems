def maxSubArray(nums):
    maxSum = nums[0]
    currSum = 0

    for num in nums:
        if currSum<0:
            currSum = 0
        currSum = currSum+num
        maxSum = max(maxSum, currSum)
    return maxSum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))