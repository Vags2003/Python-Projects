'''Given an integer array nums, 
return true if any value appears at least twice in the array,
and return false if every element is distinct.'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        nums.sort()

        for i in range (0,n-1):            
            if nums[i] == nums[i+1]:
                count = count+ 1
            
        if count >= 1:
            return True
        
        return False