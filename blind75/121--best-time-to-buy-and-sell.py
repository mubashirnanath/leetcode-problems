def maxProfit(prices):

    left, right = 0, 1
    profit = 0

    while right < len(prices):

        if prices[right] > prices[left]:
            profit = max(profit, prices[right]-prices[left])
        else:
            left = right
        right +=1
        
    return profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))