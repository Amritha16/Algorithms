# Given weights and values of n items, put these items in 
# a knapsack of capacity W to get the maximum total value in the knapsack. 
# In other words, given two integer arrays val[0..n-1] and wt[0..n-1] 
# which represent values and weights associated with n items respectively. 
# Also given an integer W which represents knapsack capacity, 
# find out the maximum value subset of val[] such that sum of the weights of this subset
#  is smaller than or equal to W. You cannot break an item, 
#  either pick the complete item or don’t pick it (0-1 property).

def knapsack(weight, wt, val, n, dp = {}):
    if not n or not weight: 
        dp[n] = 0
    if n in dp: return dp[n]
    if(wt[n - 1] > weight): 
        dp[n] = knapsack(weight, wt, val, n - 1)
    else:
        dp[n] = max(val[n - 1] + knapsack(weight - wt[n - 1], wt, val, n -1), knapsack(weight, wt, val, n - 1))
    return dp[n]

val = [60, 100, 120]
wt = [10, 20, 30]
weight = 50
print(knapsack(weight, wt, val, len(wt)))