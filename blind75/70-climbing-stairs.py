def climbStairs(n):
    """
    Calculates the number of distinct ways to climb `n` stairs.
    You can climb 1 or 2 steps at a time.
    Uses Bottom-Up Dynamic Programming (Fibonacci sequence) for O(n) time and O(1) space.
    """
    
    # Base cases:
    # 0 stairs -> 1 way (do nothing)
    # 1 stair -> 1 way (take 1 step)
    # So for n=1, the answer is 1. We start a and b at 1.
    a, b = 1, 1

    # We need to compute the sequence up to n.
    # We already have the answer for n=1 (which is b=1).
    # We need to calculate n-1 more times to reach n.
    for i in range(n - 1):
        # The number of ways to reach the current step is the sum
        # of the ways to reach the two previous steps.
        c = a + b
        
        # Shift our window forward
        a = b
        b = c
    
    # After the loop, b holds the number of ways to reach stair n
    return b

"""
Why Bottom-Up Dynamic Programming works:

- To reach step `n`, you could have come from step `n-1` (by taking a 1-step) 
  or from step `n-2` (by taking a 2-step).
- Therefore, the total ways to reach step `n` is `ways(n-1) + ways(n-2)`.
- This is exactly the Fibonacci sequence recurrence relation!
- Instead of using recursion or an array which takes O(n) space,
  we only need to keep track of the last two values (`a` and `b`).

Example walkthrough with n = 5:

  Initial state: a=1 (ways for n=0), b=1 (ways for n=1)
  
  i=0 (n=2): c = a+b = 1+1 = 2. Update a=1, b=2. (ways for n=2 is 2)
  i=1 (n=3): c = a+b = 1+2 = 3. Update a=2, b=3. (ways for n=3 is 3)
  i=2 (n=4): c = a+b = 2+3 = 5. Update a=3, b=5. (ways for n=4 is 5)
  i=3 (n=5): c = a+b = 3+5 = 8. Update a=5, b=8. (ways for n=5 is 8)
  
  Loop ends (ran n-1 = 4 times).
  Result is b = 8.

Time Complexity: O(n) - We loop n-1 times.
Space Complexity: O(1) - We only store a few variables (a, b, and c).
"""

print(climbStairs(5))