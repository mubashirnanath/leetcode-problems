"""
Problem Name: Climbing Stairs
Problem Description:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Link to Problem:
https://leetcode.com/problems/climbing-stairs/
"""

# Approach and Explanation:
"""
1. Approach:
   - This problem can be solved using dynamic programming or Fibonacci sequence logic.
   - Let dp[i] represent the number of ways to reach the i-th step.
   - Recurrence relation: dp[i] = dp[i - 1] + dp[i - 2]
     - dp[i - 1]: The number of ways to reach the i-th step by taking 1 step from (i - 1).
     - dp[i - 2]: The number of ways to reach the i-th step by taking 2 steps from (i - 2).
   - Base cases:
     - dp[0] = 1 (1 way to stay at the ground step).
     - dp[1] = 1 (1 way to reach the first step).

2. Key Observations:
   - The problem is analogous to finding the nth Fibonacci number, shifted by 1.
   - We can use an iterative approach with constant space by keeping track of the last two results.

3. Alternative Solutions:
   - Use recursion with memoization.
   - Directly compute using the closed-form Fibonacci formula (not recommended due to precision issues with large n).
"""

# Code Implementation:
def climb_stairs(n: int) -> int:
    """
    Returns the number of distinct ways to climb to the top of a staircase with n steps.
    :param n: The number of steps to the top.
    :return: The number of distinct ways to climb to the top.
    """
    if n<=1:
        return n
    a, b = 1, 1
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    return c


# Complexity Analysis:
"""
Time Complexity: O(n)
- We iterate through the steps from 3 to n.

Space Complexity: O(1)
- Only two variables are used to store the last two results.
"""
