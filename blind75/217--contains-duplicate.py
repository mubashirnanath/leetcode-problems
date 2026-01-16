def containsDuplicate(nums):
    """
    Check if array contains any duplicate values.
    Uses HashSet for O(n) time and O(n) space.
    
    Key insight: HashSet has O(1) lookup - we can check if we've seen 
    a number before in constant time.
    """
    
    # HashSet to store numbers we've seen
    hash_set = set()

    for num in nums:
        # Check if this number was already seen
        if num in hash_set:
            # Duplicate found!
            return True
        else:
            # First time seeing this number, add to set
            hash_set.add(num)
    
    # Went through all numbers without finding duplicates
    return False

"""
How HashSet approach works:
- For each number, check if it's already in the set (O(1) lookup)
- If yes → duplicate found, return True
- If no → add to set and continue
- If loop completes → no duplicates

Example with nums=[1,2,3,1]:
  num=1: not in set, add {1}
  num=2: not in set, add {1,2}
  num=3: not in set, add {1,2,3}
  num=1: already in set! Return True

Time: O(n) - single pass, O(1) set operations
Space: O(n) - storing up to n elements in set
"""

nums = [1,2,3,1]
print(containsDuplicate(nums))


# ============================================
# Alternative: One-liner using set comparison
# ============================================
def containsDuplicateSimple(nums):
    """
    Simple approach: If set size differs from array size, duplicates exist.
    
    Why it works:
    - Set removes duplicates automatically
    - If len(set) < len(array) → there were duplicates
    - If len(set) == len(array) → all unique
    """
    return len(nums) != len(set(nums))

nums = [1,2,3,1]
print(containsDuplicateSimple(nums))