class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Understand
        Input: Array of various stock prices on consecutive days
        Output: Maximum profit that can be made from buying on one day and selling on later day.
        Constraints: Sale can only be made after buying 
        '''

        min_price, max_profit = prices[0], 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit

'''
Analysis:
Avg time: O(n) because of for loop that runs for n iterations
Space: O(1) because no new data structure is created 
'''
