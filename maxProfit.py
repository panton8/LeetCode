def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    left_point = 0
    right_point = 1

    while right_point < len(prices):
        if prices[left_point] < prices[right_point]:
            current_profit = prices[right_point] - prices[left_point]
            max_profit = max(current_profit, max_profit)
        else:
            left_point = right_point
        right_point += 1

    return max_profit
