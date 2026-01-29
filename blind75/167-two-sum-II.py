def twoSum(numbers, target):
    """
    Find two numbers in a SORTED array that add up to target.
    Returns their 1-indexed positions. Uses two-pointer technique for O(n) time.
    """
    
    # Initialize two pointers: one at start, one at end
    # Since array is sorted, we can move pointers strategically
    l, r = 0, len(numbers)-1

    while l < r:
        # Calculate sum of elements at both pointers
        currSum = numbers[l] + numbers[r]

        if currSum == target:
            # Found the pair! Return 1-indexed positions (not 0-indexed)
            return [l+1, r+1]
        elif currSum > target:
            # Sum is too large, move right pointer left to decrease sum
            r -= 1
        else:
            # Sum is too small, move left pointer right to increase sum
            l += 1
    
    # No solution found (problem guarantees one exists)
    return []

"""
Why Two-Pointer works (for sorted array):
- Array is sorted, so we know moving left pointer increases sum
- Moving right pointer decreases sum
- Start from opposite ends and move toward center
- Each element is visited at most once, giving O(n) time complexity
- O(1) space complexity (no extra data structures needed)

Difference from Two Sum I:
- Two Sum I: unsorted array, needs HashMap, O(n) time, O(n) space
- Two Sum II: sorted array, uses two pointers, O(n) time, O(1) space

Example walkthrough with numbers=[2,7,11,15], target=9:
  l=0, r=3: sum=2+15=17, too large, move r left
  l=0, r=2: sum=2+11=13, too large, move r left
  l=0, r=1: sum=2+7=9, found! Return [1,2] (1-indexed)
"""

nums = [3,4,6,7,9]
print(twoSum(nums,9 ))