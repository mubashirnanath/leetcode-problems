def maxProduct(nums):

    res = nums[0]
    currMin, currMax = 1, 1

    for num in nums:
        currMax = max(currMax*num, currMin*num, num)
        currMin = min(currMax*num, currMin*num, num)

        res = max(res, currMax)
    return res


nums = [2, 3, -2, 4]
print(maxProduct(nums))