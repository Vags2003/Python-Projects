'''Given an integer array nums,
return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

    # Calculate the product of all elements to the left of each element.
        left_mul = 1
        for i in range(1, n):
            left_mul *= nums[i - 1]
            result[i] *= left_mul

    # Calculate the product of all elements to the right of each element while updating the final result.
        right_mul = 1
        for i in range(n - 2, -1, -1):
            right_mul *= nums[i + 1]
            result[i] *= right_mul

        return result
    
