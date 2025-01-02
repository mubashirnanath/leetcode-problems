"""
Problem Name: Counting Bits
Problem Description:
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Link to Problem:
https://leetcode.com/problems/counting-bits/

Date Solved:
2025-01-01
"""

# Approach and Explanation:
"""
1. Approach:
   - Use dynamic programming to calculate the number of 1's for each number from 0 to n.
   - The number of 1's for a number i can be derived from:
     ans[i] = ans[i & (i - 1)] + 1
     - ans[i & (i - 1)] gives the number of 1's by removing the least significant set bit.
     - Add 1 to account for the removed bit.

2. Key Observations:
   - The number of set bits for any number i depends on its binary representation.
   - Using the above formula, we can compute the result efficiently without recalculating.

3. Alternative Solutions:
   - Use the `bin()` function and count '1's for each number (less efficient).
"""

# Code Implementation:
def count_bits(n: int) -> list:
    """
    Returns an array where the i-th element is the number of 1's in the binary representation of i.
    :param n: A non-negative integer.
    :return: List[int] with the number of 1's for each integer from 0 to n.
    """
    bit_count = [0] * (n + 1)
    for i in range(1, n + 1):
        bit_count[i] = bit_count[i & (i - 1)] + 1
    return bit_count

# Test Cases:
if __name__ == "__main__":
    # Example test cases
    test_cases = [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (0, [0]),
        (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]),
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = count_bits(input_data)
        print(f"Test Case {i + 1}: {'Passed' if result == expected else f'Failed (Got {result}, Expected {expected})'}")

# Complexity Analysis:
"""
Time Complexity: O(n)
- We iterate through all numbers from 1 to n.
- Each computation for ans[i] is O(1).

Space Complexity: O(n)
- We use an array of size n + 1 to store results.
"""
