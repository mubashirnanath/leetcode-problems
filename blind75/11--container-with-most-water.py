# Brute force
def maxAreaBruteForce(height):
    """
    Find the maximum water a container can hold using brute force.
    Checks every possible pair of lines → O(n²) time complexity.
    """

    maxarea = 0
    n = len(height)

    # Try every pair of lines (i, j)
    for i in range(n):
        for j in range(i+1, n):
            # Height of water is limited by the SHORTER line
            h = min(height[i], height[j])
            # Width is the horizontal distance between the two lines
            w = j - i
            # Area = height × width
            area = h * w
            # Keep track of the largest area found
            maxarea = max(maxarea, area)
    return maxarea



def maxArea(height):
    """
    Find the maximum water a container can hold.
    Uses *- two-pointer technique -* for O(n) time complexity.

    Key insight: Start with the widest container (left=0, right=end).
    Then ALWAYS move the pointer pointing to the SHORTER line inward.

    Why? Because:
    - The area is limited by the shorter line.
    - Moving the taller line inward can NEVER increase the area
      (width shrinks and height stays the same or decreases).
    - Moving the shorter line inward MIGHT find a taller line,
      potentially increasing the area despite reduced width.
    """

    maxarea = 0
    # Start with the widest possible container
    l = 0                  # Left pointer at the start
    r = len(height) - 1    # Right pointer at the end

    while l < r :

        if height[l] > height[r]:
            # Right line is shorter → it limits the height
            # Area = shorter height × width
            area = height[r] * (r-l)
            # Move the shorter (right) pointer inward to try a taller line
            r -= 1

        else:
            # Left line is shorter (or equal) → it limits the height
            # Area = shorter height × width
            area = height[l] * (r-l)
            # Move the shorter (left) pointer inward to try a taller line
            l += 1
        
        # Update the maximum area found so far
        maxarea = max(maxarea, area)

    return maxarea

"""
Why move the shorter pointer?

The area formula is:  area = min(height[l], height[r]) × (r - l)

If height[l] < height[r]:
  - Moving l inward: width decreases by 1, but height MIGHT increase → area could go up
  - Moving r inward: width decreases by 1, and height stays ≤ height[l] → area ALWAYS goes down
  → So moving the shorter pointer is the only chance to find a bigger area!

Example walkthrough with height = [1, 8, 6, 2, 5, 4, 8, 3, 7]:

  l=0, r=8: h[0]=1, h[8]=7 → area=1×8=8,  maxarea=8,  move l (shorter)
  l=1, r=8: h[1]=8, h[8]=7 → area=7×7=49, maxarea=49, move r (shorter)
  l=1, r=7: h[1]=8, h[7]=3 → area=3×6=18, maxarea=49, move r (shorter)
  l=1, r=6: h[1]=8, h[6]=8 → area=8×5=40, maxarea=49, move l (equal)
  l=2, r=6: h[2]=6, h[6]=8 → area=6×4=24, maxarea=49, move l (shorter)
  l=3, r=6: h[3]=2, h[6]=8 → area=2×3=6,  maxarea=49, move l (shorter)
  l=4, r=6: h[4]=5, h[6]=8 → area=5×2=10, maxarea=49, move l (shorter)
  l=5, r=6: h[5]=4, h[6]=8 → area=4×1=4,  maxarea=49, move l (shorter)
  l=6, r=6: loop ends (l not < r)

Answer: 49 (between lines at index 1 and 8, heights 8 and 7)

Time Complexity: O(n) - each pointer moves at most n times
Space Complexity: O(1) - only a few variables
"""

nums = [1,8,6,2,5,4,8,3,7]
print(maxArea(nums))