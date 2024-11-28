'''Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = 0
        mul1 = 1
        n = len(nums)

        if n<2:
            return nums[0]
    
        for i in nums:
            mul1 = max(i, mul1 * i)
            output = max(output, mul1)
    
        return output
