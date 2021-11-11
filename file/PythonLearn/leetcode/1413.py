from typing import List


nums = [-3,2,-3,4,2]

def minStartValue(self, nums: List[int]) -> int:
    num_length = len(nums)
    dp = [0]*num_length
    for i in range(num_length):
        if i==0:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i-1]+nums[i]
    
    return 1+abs(min(dp)) if min(dp) < 0 else 1