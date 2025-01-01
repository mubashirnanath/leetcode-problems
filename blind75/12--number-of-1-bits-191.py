"""
Problem Name: Number of 1 Bits (Hamming Weight)
Problem Description:
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:
Input: n = 11 (binary: 1011)
Output: 3

Example 2:
Input: n = 128 (binary: 10000000)
Output: 1

Link to Problem:
https://leetcode.com/problems/number-of-1-bits/
"""

# Approach and Explanation:
"""
1. Approach:
   - We use a bitwise operation to count the number of '1' bits in the binary representation of the number.
   - Specifically, repeatedly applying the operation `n & (n - 1)` removes the least significant '1' bit until `n` becomes zero.
   - Count the number of such operations, which equals the number of '1' bits.

2. Key Observations:
   - The operation `n & (n - 1)` reduces `n` by removing its rightmost set bit.
   - This approach is efficient and avoids converting the number to a string.

3. Alternative Solutions:
   - Use Python's built-in `bin()` function and count the '1's in the resulting binary string (`bin(n).count('1')`).
   - Loop through each bit of the number, checking if it is set using `n & 1`, and right-shifting `n` until it becomes zero.
"""

# Code Implementation:
def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1  # Removes the rightmost set bit
        count += 1
    return count

# Complexity Analysis:
"""
Time Complexity: O(k)
- k is the number of set bits in the binary representation of n.
- Each operation `n & (n - 1)` removes one set bit, so the loop runs k times.

Space Complexity: O(1)
- No extra space is used apart from a few variables.
"""
