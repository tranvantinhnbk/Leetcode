class Solution:
    memo = {}
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0 
        elif amount < 0: 
            return -1 
        else:
            if amount in Solution.memo:
                return Solution.memo[amount]
            else:
                res_coin = [self.coinChange(coins, amount-coin) for coin in coins]
                res_coin = [val for val in res_coin if val>=0]
                if len(res_coin) == 0:
                    Solution.memo[amount] = -1
                else:
                    Solution.memo[amount] = 1 + min(res_coin)
                return Solution.memo[amount]
            
print(Solution().coinChange([2], 3))
print(Solution().coinChange([2], 3))