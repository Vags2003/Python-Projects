'''Given an integer array 'nums', find the 
subarray
 with the largest sum, and return its sum.'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = float('-inf')  
        sum1 = 0  
    
        for i in nums:
            sum1 = max(i, sum1 + i)
            output = max(output, sum1)
    
        return output
        