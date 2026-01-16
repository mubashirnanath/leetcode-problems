def productExceptSelf(nums):
    """
    Return array where each element is product of all OTHER elements.
    Uses prefix and postfix products for O(n) time WITHOUT division.
    
    Key insight: For each index i, answer = (product of all elements before i) 
                                          × (product of all elements after i)
                 We call these PREFIX and POSTFIX products.
    """

    # Initialize result array with 1s
    # This will store our answer
    res = [1] * len(nums)
    
    # ============ PASS 1: Calculate PREFIX products ============
    # prefix = product of all elements BEFORE current index
    prefix = 1
    
    for i in range(len(nums)):
        # Store prefix product at current position
        # res[i] now contains product of all elements to the LEFT of i
        res[i] = prefix
        
        # Update prefix to include current element for next iteration
        prefix = prefix * nums[i]
    
    # After Pass 1 for nums=[1,2,3,4]:
    # res = [1, 1, 2, 6]
    #        ↑  ↑  ↑  ↑
    #        1  1  1×2  1×2×3
    
    # ============ PASS 2: Multiply by POSTFIX products ============
    # postfix = product of all elements AFTER current index
    postfix = 1
    
    for i in range(len(nums) - 1, -1, -1):  # Loop backwards
        # Multiply current res[i] (prefix) by postfix
        # res[i] now = prefix × postfix = product of all except self!
        res[i] = res[i] * postfix
        
        # Update postfix to include current element for next iteration
        postfix = postfix * nums[i]
    
    # After Pass 2 for nums=[1,2,3,4]:
    # res = [24, 12, 8, 6]
    #        ↑   ↑   ↑  ↑
    #     1×24  1×12 2×4 6×1
    
    return res

"""
Visual breakdown for nums = [1, 2, 3, 4]:

Index:     0      1      2      3
Value:     1      2      3      4
           
Prefix:    1      1     1×2   1×2×3
           =1     =1     =2     =6
           
Postfix:  2×3×4  3×4    4      1
           =24    =12    =4     =1
           
Answer:   1×24   1×12   2×4    6×1
           =24    =12    =8     =6

Time Complexity: O(n) - two passes through array
Space Complexity: O(1) - output array doesn't count as extra space
"""

nums = [1,2,3,4]
print(productExceptSelf(nums))