'''Given an array of integers 'nums' and an integer 'target',
return indices of the two numbers such that they add up to target.'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        n = len(nums)
        l = []
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    l.append(i) 
                    l.append(j)
                    count+=1
            if count == 1:
                return l