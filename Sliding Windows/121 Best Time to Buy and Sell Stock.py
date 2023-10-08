# 121. Best Time to Buy and Sell Stock
def maxProfit(prices):

    ans = 0
    l, r = 0, 1

    while r < len(prices):
        if prices[r] <= prices[l]:
            l = r
        else: 
            ans = max(ans, prices[r]-prices[l])
        r += 1
        
    return ans


def maxProfit2(prices):
    res = 0

    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res, price - lowest)
    return res