class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        '''
        set is a python data structure that stores 
        - unique values only
        - no duplicates
        - unordered
        - very fast lookup (avg O(1))
        when checking duplicates 
        - the first time u see a number --> store it 
        - the second time you see it --> duplicate found
        '''
        for x in nums: 
            if x in seen: 
                return True
            seen.add(x)
        return False