'''You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        
        jump = nums[0]
        for i in range(1,n):
            if i > jump:
                return False
            
            jump = max(jump, i+nums[i])

            if jump >= n-1:
                return True
        return False