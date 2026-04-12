class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            count=0  
            for j in range(len(nums)): 
                if nums[i]==nums[j]: 
                    count+=1
                    if count>=2:
                        return True 
    
        return False