#User function Template for python3
class Solution:
    def minCost(self, height):
        # code here
        '''
        Mooisation
        '''
        # dp = [-1]*len(height)
        # def f(i):
        #     if i == 0:return 0
        #     if dp[i] != -1: return dp[i]
        #     l = f(i-1)+abs(height[i-1]-height[i])
        #     if i>1:
        #         r = f(i-2)+abs(height[i-2]-height[i])
        #     else:
        #         r = float('inf')
        #     dp[i] = min(l,r)    
        #     return dp[i]
        
        '''
        Tabulation
        '''
        # dp = [0]*len(height)
        # for i in range(1,len(height)):
        #     if i == 1:
        #         dp[i] = abs(height[i-1]-height[i])
        #     else:
        #         dp[i] = min(dp[i-1]+abs(height[i]-height[i-1]),dp[i-2]+abs(height[i]-height[i-2]))
        # return dp[-1]   
        '''
        Tabulation Space Optimized`
        '''
        if len(height)<=1:
            return 0
        prev = 0
        prev2 = abs(height[1]-height[0])
        for i in range(1,len(height)):
            cur = min(prev+abs(height[i]-height[i-1]),prev2+abs(height[i]-height[i-2]))
            prev2 = prev
            prev = cur
        return prev
        
