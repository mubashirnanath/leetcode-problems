def findMin(nums):

    res = nums[0]
    l = 0
    r = len(nums) - 1

    while l<=r:
        if nums[l]<=nums[r]:        # check the array or current subarray is sorted or not
            res = min(res, nums[l])
            break

        mid = (l+r)//2
        res = min(res, nums[mid])

        if l<=mid: # sorted array
            # goto right
            l = mid+1
        else:
            # goto left
            r = mid - 1
        
    return res

nums = [4,5,6,7,0,1,2]
print(findMin(nums))