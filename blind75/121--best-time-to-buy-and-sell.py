def maxProfit(prices):
    """
    Find the maximum profit from buying and selling stock once.
    Uses two-pointer/sliding window technique for O(n) time.
    Key insight: Buy low, sell high - find the best buy day and best sell day after it.
    """

    # Two pointers: left = buy day, right = sell day
    # We try to find the minimum buy price and maximum profit
    left, right = 0, 1
    profit = 0  # Track maximum profit found so far

    while right < len(prices):
        # Calculate profit if we buy at 'left' and sell at 'right'
        currentProfit = prices[right] - prices[left]

        if prices[right] > prices[left]:
            # We can make profit! Update max if this is better
            profit = max(profit, currentProfit)
        else:
            # prices[right] <= prices[left]
            # Found a lower price! Move buy pointer here
            # Why? Any future profit will be higher if we buy at this lower price
            left = right
        
        # Move sell pointer forward to check next day
        right += 1
        
    return profit

"""
Why this works (Sliding Window approach):
- We want: max(prices[j] - prices[i]) where j > i
- Keep track of minimum price seen so far (left pointer)
- For each new price, calculate profit from that minimum
- If we find a new minimum, update left pointer

Example walkthrough with prices=[7,1,5,3,6,4]:
  left=0(7), right=1(1): 1<7, move left to 1
  left=1(1), right=2(5): profit=5-1=4 ✓
  left=1(1), right=3(3): profit=3-1=2 (not better)
  left=1(1), right=4(6): profit=6-1=5 ✓ (best!)
  left=1(1), right=5(4): profit=4-1=3 (not better)
  Answer: 5
"""

prices = [7,1,5,3,6,4]
print(maxProfit(prices))